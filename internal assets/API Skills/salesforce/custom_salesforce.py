from dotenv import load_dotenv
from simple_salesforce import Salesforce
import os

load_dotenv()

username = os.getenv('SF_USERNAME', '')
print(username)
password = os.getenv('SF_PASSWORD', '')
token = os.getenv('SF_TOKEN', '')


#######SALESFORCE CREDENTIALS########
try:        
    sf = Salesforce(username=username, password=password, security_token=token)
except:
    print("Ensure you have entered the correct credentials for Salesforce")

#####SALESFORCE PRICEBOOK AND PRODUCT RELATION######
unit_price_query = """SELECT Id, Name, UnitPrice, IsActive, PriceBook2Id FROM PricebookEntry WHERE Name='Xtralife' AND UnitPrice>0.0 ORDER BY UnitPrice"""
pb_query = """SELECT Id, Name from Pricebook2 WHERE Id = '{text}'"""

def get_all_price_book():
    result = sf.query(unit_price_query)
    products = []

    for row in result["records"]:
        pb_query_replaced = pb_query.format(text=row["Pricebook2Id"])
        pb_result = sf.query(pb_query_replaced)
        pricebook_name = pb_result["records"][0]["Name"] if pb_result["records"] else "Unknown"

        products.append({
            "products_data": row,
            "Pricebook Name": pricebook_name
        })
    return products

#####SALESFORCE ORDER APIs######

def get_all_orders():
    order_query = """SELECT Id, OrderNumber, TotalAmount from Order"""
    order_result = sf.query(order_query)

def create_order(account_id, date, Pricebook2Id, status="Draft"):
    order_result = sf.Order.create({
        'AccountId': account_id,  # Account associated with the order, eg '001IU00002pmnF0YAI'
        'EffectiveDate': date,  # Effective date of the order, eg '2025-03-10'
        'Status': status,  # You can set it to 'Draft' initially,
        'Pricebook2Id': Pricebook2Id,
    })

    return sf.Order.create({
        'AccountId': account_id,  # Account associated with the order, eg '001IU00002pmnF0YAI'
        'EffectiveDate': date,  # Effective date of the order, eg '2025-03-10'
        'Status': status,  # You can set it to 'Draft' initially,
        'Pricebook2Id': Pricebook2Id,
    })


def create_order_item(order_id, product_id, unit_price, pricebookEntry_id, quantity):
    #order: use get order skill from wxo
    #product: use get product skills from wxo
    #unit_price:
    order_item = {
    'OrderId': order_id,
    'Product2Id': product_id,
    'Quantity': quantity,
    'UnitPrice': unit_price, #result['records'][0]["UnitPrice"],
    'PriceBookEntryID':pricebookEntry_id
}
    sf.OrderItem.create(order_item)
