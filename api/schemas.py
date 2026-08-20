from pydantic import BaseModel

class CustomerData(BaseModel):
    credit_score: int
    age: int
    tenure: int
    balance: float
    num_of_products: int
    has_cr_card: int
    is_active_member: int
    estimated_salary: float
    geography: str
    gender: str

class ChurnPredictionResponse(BaseModel):
    churn_probability: float
    prediction: str