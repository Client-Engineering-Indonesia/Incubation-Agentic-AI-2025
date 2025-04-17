import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from crewai import Agent, Task, Crew, Process
from crewai import LLM
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class QueryRequest(BaseModel):
    query: str

# Load environment variables
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM
llm = LLM(
    api_key = os.getenv("WATSONX_API_KEY", None),
    model= "watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", 
    # "meta-llama/llama-3-3-70b-instruct", "watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", "meta-llama/llama-3-3-70b-instruct",
    #llama-4-maverick-17b-128e-instruct-fp8 llama-4-scout-17b-16e-instruct meta-llama/llama-3-3-70b-instruct
#'meta-llama/llama-4-maverick-17b-128e-instruct-fp8', 'meta-llama/llama-4-scout-17b-16e-instruct', 
    params={
        "decoding_method": "greedy",
        "max_new_tokens": 15000,
        "temperature": 0,
        "repetition_penalty": 1.05
    }
)

def get_db_connection():
    return sqlite3.connect('sales.db')

# SQL Query Generator Agent
def create_query_generator():
    return Agent(
        role="SQL Query Generator",
        goal="Convert natural language queries into optimized SQL queries",
        backstory="""Kamu adalah seorang developer SQL yang mempunyai keahlian untuk merubah pertanyaan user menjadi suatu kueri SQL yang efisien. Kamu memahami hubungan data yang kompleks dan mampu membuat kueri yang melibatkan agregasi, pengelompokan (grouping), dan operasi tanggal. Selalu gunakan nama kolom 'month_year' dan 'total_figure' secara konsisten.""",
        llm=llm,
        allow_delegation=False
    )

def create_generation_task(agent, query):
    return Task(
        description=f"""Convert the following natural language query into a SQL query:
        
        Natural Query: {query}
        
        Database Schema:
        Table: Sales
        Columns:
        - ID (INTEGER PRIMARY KEY)
        - Order ID (TEXT)
        - Order Date (TEXT, Format: YYYY-MM-DD)
        - Ship Date (TEXT, Format: YYYY-MM-DD)
        - Ship Mode (TEXT)
        - Customer ID (TEXT)
        - Customer Name (TEXT)
        - Segment (TEXT)
        - Country (TEXT)
        - City (TEXT)
        - State (TEXT)
        - Postal Code (TEXT)
        - Region (TEXT)
        - Product Name (TEXT) includes 'Xtralife'
        - Product_ID (TEXT)
        - Category (TEXT)
        - Sub Category (TEXT)
        - Sales (REAL)
        - Quantity (INTEGER)
        - Discount (REAL)
        - Profit (REAL)
        
        Requirements:
        1. Column Names:
           - Always use exact column names as shown in above schema.
           - Always use meaningful aliases for aggregated columns
           - Example: SUM(Sales) as total_sales, AVG(Profit) as avg_profit

        2. Date Operations:
           - Always use fixed YYYY-MM values for complete month queries
           - Format for complete months: strftime('%Y-%m', `Order Date`)
           - Use >= and <= instead of BETWEEN

        3. Time Window Patterns:
           - For last N complete months:
             strftime('%Y-%m', "Order Date") >= strftime('%Y-%m', date('now', '-N months')) AND strftime('%Y-%m', "Order Date") < strftime('%Y-%m', date('now'))
           - For last month:
             strftime('%Y-%m', `Order Date`) = (SELECT strftime('%Y-%m', date('now', '-1 month')))
           - For last year this month:
             strftime('%Y-%m', `Order Date`) = (SELECT strftime('%Y-%m', date('now', '-1 year')))
        
        4. Aggregations:
           - Always include GROUP BY when using aggregate functions
           - Example: SELECT `Product Name`, SUM(Sales) as total_figure FROM Sales GROUP BY `Product Name`
        
        5. Filtering:
           - Use HAVING for filtering aggregated results
           - Use WHERE for filtering raw data
           - Example: HAVING total_sales > 1000
        
        6. Sorting:
           - Specify sort direction (ASC/DESC)
           - Example: ORDER BY total_figure DESC
        

        Output the SQL query only, without any additional text or explanations.""",
        expected_output="""A valid SQL query that accurately represents the natural language request.""",
        agent=agent
    )

import re
def clean_sql(sql: str) -> str:
    # Remove triple backticks and optional "sql" label
    return re.sub(r"```(?:sql)?|```", "", sql).strip()

@app.post("/query") 
async def process_query(request: QueryRequest):
    try:
        query_generator = create_query_generator()
        generation_task = create_generation_task(query_generator, request.query)
        
        generation_crew = Crew(
            agents=[query_generator],
            tasks=[generation_task],
            process=Process.sequential,
            verbose=True
        )
        
        sql_query = str(generation_crew.kickoff()).strip()
        sql_query = clean_sql(sql_query)  # ← sanitize the LLM output
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            columns = [description[0] for description in cursor.description]
            results = cursor.fetchall()
            formatted_results = [dict(zip(columns, row)) for row in results]

        return {"result": formatted_results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
