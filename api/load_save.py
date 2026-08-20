import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / 'models'

preprocessor = joblib.load(MODEL_DIR / 'preprocessor.pkl')
model = joblib.load(MODEL_DIR / 'gradient_boosting_model.pkl')
threshold = joblib.load(MODEL_DIR / 'threshold.pkl')



