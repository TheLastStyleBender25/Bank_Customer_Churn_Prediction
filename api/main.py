from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from api.routes import router as PredictionRouter
from api.limiter import limiter

app = FastAPI(title="Bank Customer Churn Prediction API", description="API for predicting bank customer churn", version="1.0.0")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(PredictionRouter)