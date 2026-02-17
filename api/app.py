from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from analyze import analyze

app = FastAPI(title="TradeMind API")

# -------------------------------
# CORS Middleware
# -------------------------------
# Allows frontend applications to communicate with this backend.
# In production, replace "*" with your frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Schema
# -------------------------------
class AnalyzeRequest(BaseModel):
    ticker: str

# -------------------------------
# Health Check Endpoint
# -------------------------------
@app.get("/")
def health():
    return {"status": "TradeMind API is running"}

# -------------------------------
# Stock Analysis Endpoint
# -------------------------------
@app.post("/analyze")
def analyze_stock(request: AnalyzeRequest):
    try:
        result = analyze(request.ticker)

        if not isinstance(result, dict):
            raise ValueError("Analyze function did not return JSON.")

        return result

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )
