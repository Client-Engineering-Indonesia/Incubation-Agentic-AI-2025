from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from crewai import Agent, Task, Crew, Process
from crewai import LLM
import os
import json

# Load environment variables
load_dotenv()

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ReorderQuantityRequest(BaseModel):
    current_inventory: int
    historic_data: int
    forecast: int  


# WatsonX LLM Initialization
llm = LLM(
    api_key=os.environ["WATSONX_API_KEY"],
    model=os.environ["MODEL_ID"],
    params={
        "decoding_method": "greedy",
        "max_new_tokens": 500,
        "temperature": 0,
        "repetition_penalty": 1.05
    }
)


# Inventory Optimization Agent
def create_inventory_agent():
    return Agent(
        role="Inventory Optimizer",
        goal="Determine optimal reorder quantity to maintain ideal stock levels.",
        backstory="""You are an AI-powered inventory manager. Your goal is to calculate 
        the reorder quantity using past trends and forecasted demand. Avoid stock shortages 
        while preventing excess inventory. Explain your decision based on data patterns.""",
        llm=llm,
        allow_delegation=False
    )

# Task Definition
def create_inventory_task(agent, current_inventory, historic_data, forecast):
    return Task(
        description=f"""
Given the following data:
- Current Inventory: {current_inventory}
- Quantity sold previous month: {historic_data}
- Forecasted Quantity for next month: {forecast}

Determine the optimal reorder quantity to ensure sufficient stock while minimizing excess inventory.
Instructions for calculating the optimal reorder quantity:
1. Shortfall calculation.
    - Shortfall = Forecast - Inventory
2. Saftey stock calculation
    - If shortfall <= historic sales:
        Saftety Stock = 10% of historic sales
        Reorder Quantity = Shortfall + Safety Stock
    - If shortfall > historic sales:
        Reorder Quantity = Shortfall

Provide a structured response in JSON format with:
1. "reorder_quantity": An integer representing the reorder quantity.
2. "reasoning": A detailed explanation for why this reorder quantity was chosen.
        """,
        expected_output='''A JSON object: 
        {
          "reorder_quantity": <integer>,
          "reasoning": "<string explanation>"
        }''',
        agent=agent
    )

@app.post("/calculate-reorder-quantity")
def calculate_reorder_quantity(request:ReorderQuantityRequest):
    inventory_agent = create_inventory_agent()
    inventory_task = create_inventory_task(inventory_agent, 
                                            request.current_inventory, 
                                            request.historic_data, 
                                            request.forecast)

    # Create and execute CrewAI workflow
    inventory_crew = Crew(
        agents=[inventory_agent],
        tasks=[inventory_task],
        process=Process.sequential,
        verbose=True
    )

    response = str(inventory_crew.kickoff()).strip()
    response = json.loads(response)
    return {"reorder_quantity":response['reorder_quantity'],
            "reasoning":response['reasoning']}
