# main.py

import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="ChronoMind Prediction API",
    description="AI-powered probabilistic prediction engine",
    version="0.1.0"
)

# Import routers
from routes.auth import router as auth_router
from routes.predictions import router as predictions_router
from routes.payments import router as payments_router
from routes.feedback import router as feedback_router

# Include routers with prefixes and tags
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(predictions_router, prefix="/predict", tags=["Predictions"])
app.include_router(payments_router, prefix="/subscribe", tags=["Payments"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])

# Database initialization on startup
from db.session import init_db

@app.on_event("startup")
async def on_startup():
    init_db()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to ChronoMind AI Prediction Backend 🚀"}
