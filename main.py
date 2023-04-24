from fastapi import FastAPI
from enum import Enum
import pickle
from Inputs import inputs
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    'http://localhost:3001',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def home():
    return " Welcome Home "

@app.post('/predict')
def predict_banknote(data:inputs):
    data = data.dict()

    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }


