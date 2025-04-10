import requests
import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce

load_dotenv()
username = os.environ.get('SF_USERNAME', '')
password = os.environ.get('SF_PASSWORD', '')
token = os.environ.get('SF_TOKEN', '')
ibm_api_key = os.environ.get('IBM_API_KEY', '')

unit_price_query = """SELECT Id, Name, UnitPrice, IsActive, PriceBook2Id FROM PricebookEntry WHERE Name='Xtralife' AND UnitPrice>0.0 ORDER BY UnitPrice"""
pb_query = """SELECT Id, Name from Pricebook2 WHERE Id = '{text}'"""

#######SALESFORCE CREDENTIALS########
try:        
    sf = Salesforce(username=username, password=password, security_token=token)
except:
    print("Ensure you have entered the correct credentials for Salesforce")

def generate_bearer_token():
#you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx)
    #API_KEY = ibm_api_key
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":ibm_api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    return mltoken

def run_agent_model(mltoken, query, role='user'):
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE:  manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"messages":[{"content":query,"role":role}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9cacf1cd-d703-47a8-bbc4-ca64fa6377f0/ai_service?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})

    print("Scoring response")
    try:
        return response_scoring.json()
    except ValueError:
        return response_scoring.text
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_all_price_book():
    result = sf.query(unit_price_query)
    products = []

    for row in result["records"]:
        pb_query_replaced = pb_query.format(text=row["Pricebook2Id"])
        pb_result = sf.query(pb_query_replaced)
        pricebook_name = pb_result["records"][0]["Name"] if pb_result["records"] else "Unknown"

        products.append({
            #"Product Name": row["Name"],
            "Unit Price": row["UnitPrice"],
            #"Pricebook ID": row["Pricebook2Id"],
            "Pricebook Name": pricebook_name
        })
    return products

def research_suppliers(user_query):
    products = get_all_price_book()
    prompt = f" {user_query} Rate the suppliers from top to bottom based on best to worst choice and also share the reasoning. The pricing information for suppliers is as follows: {products}. Look into the procurement rules and sales reviews of these suppliers into account as well."
    token = generate_bearer_token()
    response = run_agent_model (token, prompt)
    rating = response['choices'][0]['message']['content']
    # add llm to extract top supplier
    return rating


# print (researchsuppliers("Research the suppliers for Xtralife."))