from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from crewai import Agent, Task, Crew, Process
from crewai import LLM
import os
import json
import re

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
class ReorderQuantityRequest(BaseModel):
    current_inventory: int
    historic_data: int
    forecast: int  


# WatsonX LLM Initialization
llm = LLM(
    api_key=os.getenv("WATSONX_API_KEY"),
    model=os.getenv("MODEL_ID"),
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    url=os.getenv("WATSONX_URL"),
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
        goal="Menentukan jumlah pemesanan ulang yang optimal untuk mempertahankan tingkat stok yang ideal.",
        backstory="""Anda adalah manajer inventaris yang didukung AI. 
        Sasaran Anda adalah menghitung jumlah pemesanan ulang menggunakan tren masa lalu dan perkiraan permintaan. 
        Hindari kekurangan stok sekaligus mencegah kelebihan inventaris. 
        Jelaskan keputusan Anda berdasarkan pola data.""",
        llm=llm,
        allow_delegation=False
    )

# Task Definition
def create_inventory_task(agent, current_inventory, historic_data, forecast):
    return Task(
        description=f"""
Diberikan data sebagai berikut:
- Persediaan terkini: {current_inventory}
- Jumlah presediaan terjual pada bulan lalu: {historic_data}
- Prediksi persediaan terjuanl di bulan depan: {forecast}

Tentukan jumlah pemesanan ulang yang optimal untuk memastikan stok yang cukup sambil meminimalkan kelebihan inventaris.
Petunjuk untuk menghitung jumlah pemesanan ulang yang optimal:

1. Perhitungan kekurangan.
- Kekurangan = Perkiraan - Inventaris

2. Perhitungan stok pengaman
- Jika kekurangan <= penjualan historis:
  Stok Pengaman = 10% dari penjualan historis
  Jumlah Pemesanan Ulang = Kekurangan + Stok Pengaman
- Jika kekurangan > penjualan historis:
  Jumlah Pemesanan Ulang = Kekurangan

Berikan respons terstruktur dalam format JSON dengan:

1. "reorder_quantity": Bilangan bulat yang mewakili jumlah pemesanan ulang.
2. "reasoning": Penjelasan terperinci tentang mengapa jumlah pemesanan ulang ini dipilih.
        """,
        expected_output='''
        {
          "reorder_quantity": <hasil dalam bentuk bilangan bulat>,
          "reasoning": "<penjelasan secara sistematis dalam bentuk string>"
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
    print("response", response)

    #match = re.search(r'json\s*(\{.*?\})\s*', response, re.DOTALL)

    #json_str = match.group(0)
    
    data = json.loads(response)

    return {"reorder_quantity":data['reorder_quantity'],
            "reasoning":data['reasoning']}
