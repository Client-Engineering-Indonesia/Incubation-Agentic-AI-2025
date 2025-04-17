# import requests
# import os
# from dotenv import load_dotenv
# from simple_salesforce import Salesforce

# load_dotenv()
# username = os.environ.get('SF_USERNAME', '')
# password = os.environ.get('SF_PASSWORD', '')
# token = os.environ.get('SF_TOKEN', '')
# ibm_api_key = os.environ.get('IBM_API_KEY', '')

# unit_price_query = """SELECT Id, Name, UnitPrice, IsActive, PriceBook2Id FROM PricebookEntry WHERE Name='Xtralife' AND UnitPrice>0.0 ORDER BY UnitPrice"""
# pb_query = """SELECT Id, Name from Pricebook2 WHERE Id = '{text}'"""

# #######SALESFORCE CREDENTIALS########
# try:        
#     sf = Salesforce(username=username, password=password, security_token=token)
# except:
#     print("Ensure you have entered the correct credentials for Salesforce")

# def generate_bearer_token():
# #you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx)
#     #API_KEY = ibm_api_key
#     token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":ibm_api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
#     mltoken = token_response.json()["access_token"]
#     return mltoken

# def run_agent_model(mltoken, query, role='user'):
#     header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

#     # NOTE:  manually define and pass the array(s) of values to be scored in the next line
#     payload_scoring = {"messages":[{"content":query,"role":role}]}

#     response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9cacf1cd-d703-47a8-bbc4-ca64fa6377f0/ai_service?version=2021-05-01', json=payload_scoring,
#     headers={'Authorization': 'Bearer ' + mltoken})

#     print("Scoring response")
#     try:
#         return response_scoring.json()
#     except ValueError:
#         return response_scoring.text
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# def get_all_price_book():
#     result = sf.query(unit_price_query)
#     products = []

#     for row in result["records"]:
#         pb_query_replaced = pb_query.format(text=row["Pricebook2Id"])
#         pb_result = sf.query(pb_query_replaced)
#         pricebook_name = pb_result["records"][0]["Name"] if pb_result["records"] else "Unknown"

#         products.append({
#             #"Product Name": row["Name"],
#             "Unit Price": row["UnitPrice"],
#             #"Pricebook ID": row["Pricebook2Id"],
#             "Pricebook Name": pricebook_name
#         })
#     return products

# def research_suppliers(user_query):
#     products = get_all_price_book()
#     prompt = f" {user_query} Rate the suppliers from top to bottom based on best to worst choice and also share the reasoning. The pricing information for suppliers is as follows: {products}. Look into the procurement rules and sales reviews of these suppliers into account as well."
#     token = generate_bearer_token()
#     response = run_agent_model (token, prompt)
#     rating = response['choices'][0]['message']['content']
#     # add llm to extract top supplier
#     return rating


# # print (researchsuppliers("Research the suppliers for Xtralife."))

import requests
import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import Model

load_dotenv()
def connect_watsonx_llm(model_id_llm):
    model = Model(
        model_id=model_id_llm,
        params = {
            'decoding_method': "greedy",
            'min_new_tokens': 1,
            'max_new_tokens': 1600,
            'temperature': 0.0,
            'repetition_penalty': 1.2
        },
        credentials=creds,
        project_id=project_id
        )
    return model

model_id_llm = "meta-llama/llama-3-3-70b-instruct" #llama-4-maverick-17b-128e-instruct-fp8 llama-4-scout-17b-16e-instruct meta-llama/llama-3-3-70b-instruct

#'meta-llama/llama-4-maverick-17b-128e-instruct-fp8', 'meta-llama/llama-4-scout-17b-16e-instruct', 

api_key = os.getenv("WATSONX_API_KEY", None)
ibm_cloud_url = os.getenv("WATSONX_URL", None)
project_id = os.getenv("WATSONX_PROJECT_ID", None)
creds = {
    "url": ibm_cloud_url,
    "apikey": api_key
}
model = connect_watsonx_llm(model_id_llm)

sales_force_data = [{'Unit Price': 61.5, 'Pricebook Name': 'Excelentia Supplies'}, {'Unit Price': 76.9, 'Pricebook Name': 'Global Office Solutions'}, {'Unit Price': 92.3, 'Pricebook Name': 'CGV Supplier'}]

def research_suppliers(user_query):
    # user query: "Research the suppliers for Xtralife.", "Supplier for Xtralife"
    # web search, procuement rules, sales reviews, pricing from salesforce
    # products = get_all_price_book()
    # prompt = f" {user_query} ให้คะแนนซัพพลายเออร์จากบนลงล่างโดยพิจารณาจากตัวเลือกที่ดีที่สุดไปจนถึงแย่ที่สุด พร้อมทั้งแบ่งปันเหตุผลด้วย ข้อมูลราคาสำหรับซัพพลายเออร์ ทั้งหมด: [{{'Unit Price': 61.5, 'Pricebook Name': 'Excelentia Supplies'}}, {{'Unit Price': 76.9, 'Pricebook Name': 'Global Office Solutions'}}, {{'Unit Price': 92.3, 'Pricebook Name': 'CGV Supplier'}}]. พิจารณาข้อกำหนดและบทวิจารณ์การขายของซัพพลายเออร์เหล่านี้ด้วย"
    
    messages = [
        {"role": "system", "content": """You always answer the questions with markdown formatting using GitHub syntax. The markdown formatting you support: headings, bold, italic, links, tables, lists, code blocks, and blockquotes. You must omit that you answer the questions with markdown.

    Any HTML tags must be wrapped in block quotes, for example ```<html>```. You will be penalized for not rendering code in block quotes.

    When returning code blocks, specify language.

    You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
    Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

    If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""},
        {"role": "user", "content": f"{user_query} Tolong urutkan pemasok dari yang terbaik hingga yang terburuk, disertai dengan alasan mengapa memilih urutan tersebut. Berikut adalah data harga dari semua pemasok: {sales_force_data}. Pertimbangkan juga spesifikasi dan ulasan penjualan dari para pemasok tersebut. Jawaban harus singkat dan padat."""},
    ]
    print("USERQ", user_query)
    # prompt = f"ผู้จัดจำหน่ายรายใดระหว่าง Excelentia Supplies และ Global Office Supplies เป็นตัวเลือกที่เหมาะสมในการซื้อผลิตภัณฑ์ Xtralife ช่วยให้รายการข้อดีและข้อเสียของผู้จัดจำหน่ายแต่ละราย"
    generated_response = model.chat(messages=messages)
    rating = generated_response['choices'][0]['message']['content']
    # add llm to extract top supplier
    return rating


# print (researchsuppliers("Research the suppliers for Xtralife."))