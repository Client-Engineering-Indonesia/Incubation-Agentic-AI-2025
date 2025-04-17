from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#from custom_salesforce import get_all_price_book, get_all_orders, create_order, create_order_item
from simple_salesforce import Salesforce
import os
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

from dotenv import load_dotenv
load_dotenv()

username = os.getenv('SF_USERNAME', '')
print(username)
password = os.getenv('SF_PASSWORD', '')
token = os.getenv('SF_TOKEN', '')

class OrderRequest(BaseModel):
    account_id: str
    date: str
    status: str 
    Pricebook2Id: str
    Product2Id: str
    Quantity: float


#######SALESFORCE CREDENTIALS########
try:        
    sf = Salesforce(username=username, password=password, security_token=token)
except:
    print("Ensure you have entered the correct credentials for Salesforce")

#####SALESFORCE PRICEBOOK AND PRODUCT RELATION######
unit_price_query = """SELECT Id, Name, UnitPrice, IsActive, PriceBook2Id FROM PricebookEntry WHERE UnitPrice>0.0 ORDER BY UnitPrice"""
#unit_price_query = """SELECT Id, Name, IsActive, IsStandard FROM Pricebook2"""
pb_query = """SELECT Id, Name from Pricebook2 WHERE Id = '{text}'"""

def get_all_price_book():
    result = sf.query(unit_price_query)
    products = []

    for row in result["records"]:
        #pb_query_replaced = pb_query.format(text=row["Pricebook2Id"])
        #pb_result = sf.query(pb_query_replaced)
        #pricebook_name = pb_result["records"][0]["Name"] if pb_result["records"] else "Unknown"

        products.append({
            "products_data": row,
            #"Pricebook Name": pricebook_name
        })
    return products

def get_price_by_id(id):
    single_unit_price_query = f"""SELECT Id, Name, UnitPrice, IsActive, PriceBook2Id FROM PricebookEntry WHERE Id='{id}' ORDER BY UnitPrice"""
    result = sf.query(single_unit_price_query)
    products = []

    for row in result["records"]:
        #pb_query_replaced = pb_query.format(text=row["Pricebook2Id"])
        #pb_result = sf.query(pb_query_replaced)
        #pricebook_name = pb_result["records"][0]["Name"] if pb_result["records"] else "Unknown"

        products.append({
            "products_data": row,
            #"Pricebook Name": pricebook_name
        })
    return products

def create_order_item_sf(order_id, Product2Id, Quantity, UnitPrice):

    order_item = sf.OrderItem.create({
        'OrderId': order_id,
        'Product2Id': Product2Id, # by default 01uIU00000AWHg5YAH
        'Quantity': Quantity,
        'UnitPrice': UnitPrice, #result['records'][0]["UnitPrice"],
    })

    return order_item

#####SALESFORCE ORDER APIs######

def get_all_accounts_sf():
    account_query = """SELECT Id, Name, Type, Industry, CreatedDate FROM Account ORDER BY CreatedDate DESC LIMIT 100"""
    account_result = sf.query(account_query)

    return account_result

def get_all_orders_sf():
    order_query = """SELECT Id, OrderNumber, TotalAmount, CreatedDate FROM Order WHERE TotalAmount > 0 ORDER BY CreatedDate DESC LIMIT 100"""
    order_result = sf.query(order_query)

    return order_result

def create_order_sf(account_id, date, Pricebook2Id, status="Draft"):
    order_result = sf.Order.create({
        'AccountId': account_id,  # Account associated with the order, eg '001IU00002pmnF0YAI'
        'EffectiveDate': date,  # Effective date of the order, eg '2025-03-10'
        'Status': status,  # You can set it to 'Draft' initially,
        'Pricebook2Id': Pricebook2Id,
    })

    return order_result

@app.get("/")
def home():
    print("Salesforce custom skills for wxo")

# Define a route to call the check_reorder_quantity function
@app.get("/get_all_price_book")
def fetch_price_books():
    return {"price_books": get_all_price_book()}

# Define a route to call the check_reorder_quantity function
@app.get("/get_all_orders")
def get_all_orders():
    return {"orders": get_all_orders_sf()}


@app.get("/get_all_accounts")
def get_all_accounts():
    return {"accounts": get_all_accounts_sf()}

@app.post("/create_order_item/")
def create_product_in_order(request: OrderRequest):
    order = create_order_sf(
        request.account_id, # by default 001IU00002oGjMKYA0
        request.date, 
        request.Pricebook2Id # by default 01sIU00000F3uJFYAZ
    )

    print("order", order)
    

    price = get_price_by_id(request.Product2Id)[0]["products_data"]["UnitPrice"]
    #print("price", price)

    #order_id = order["id"]
    order_id = '801IU000005RLxsYAG'

    order_item = create_order_item_sf(
        order_id, 
        request.Product2Id, 
        request.Quantity, 
        price
    ) 
    

    return {"result": order_item}


# Run the FastAPI application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)