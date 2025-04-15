from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent_lab import research_suppliers

app = FastAPI()

# Add CORS middleware to allow requests from any origin with any method (you can customize as needed)
origins = ["*"]  # Allow requests from any origin
# Add CORS middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/researchsuppliers/")
async def supplier_research(query: str):
    res = {"Agent Response": research_suppliers(query)}
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
