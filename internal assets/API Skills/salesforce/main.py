from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from custom_salesforce import get_all_price_book, get_all_orders, create_order_item

# Create an instance of FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    print("Salesforce custom skills for wxo")

# Define a route to call the check_reorder_quantity function
@app.get("/pricebooks")
def fetch_price_books():
    return {"price_books": get_all_price_book()}

@app.post("/create_order_item/")
def create_product_in_order(order, product, unit_price, pricebookEntry, quantity):
    create_order_item(order, product, unit_price, pricebookEntry, quantity)

# Run the FastAPI application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)