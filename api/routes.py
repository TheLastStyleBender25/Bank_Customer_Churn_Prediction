from fastapi import APIRouter, Request
from api.limiter import limiter
from api.schemas import ChurnPredictionResponse, CustomerData
from api.load_save import preprocessor, model, threshold
import pandas as pd
from fastapi import HTTPException


router = APIRouter(prefix='/predict', tags=['Churn Prediction'])

@router.post("/", response_model=ChurnPredictionResponse)
@limiter.limit("10/minute")
async def predict(request:Request, data: CustomerData):
    customer_data = pd.DataFrame([{
        "CreditScore": data.credit_score,
        "Age": data.age,
        "Tenure": data.tenure,
        "Balance": data.balance,
        "NumOfProducts": data.num_of_products,
        "HasCrCard": data.has_cr_card,
        "IsActiveMember": data.is_active_member,
        "EstimatedSalary": data.estimated_salary,
        "Geography": data.geography,
        "Gender": data.gender
    }])

    try:
        x_processed = preprocessor.transform(customer_data)
        probability = model.predict_proba(x_processed)[0,1]

        if probability > threshold:
            prediction = 'Churn'
        else:
            prediction = 'Stay'

        return ChurnPredictionResponse(churn_probability=probability, prediction=prediction)

    except Exception as e:
        raise HTTPException(status_code=500, detail='Unable to generate churn prediction')



