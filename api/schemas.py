from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    credit_score: int = Field(..., ge=300, le=850)
    age: int = Field(..., ge=18)
    tenure: int = Field(..., ge=0, le=10)
    balance: float = Field(..., ge=0)
    num_of_products: int = Field(..., ge=1)
    has_cr_card: int = Field(..., ge=0, le=1)
    is_active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)
    geography: str
    gender: str

class ChurnPredictionResponse(BaseModel):
    churn_probability: float
    prediction: str