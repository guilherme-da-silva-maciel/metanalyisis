from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyrebase
import firebase_admin
from firebase_admin import credentials
import json
from api.routes.api import api_router
from core.configs import settings

if not firebase_admin._apps:
  cred = credentials.Certificate('metanalysis_service_account_keys.json')
  firebase = firebase_admin.initialize_app(cred)
  pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))

app = FastAPI(title="Metanalysis - review for movies")
app.include_router(api_router,prefix=settings.API_URL_STR)
app.add_middleware(CORSMiddleware,allow_origins=['* '],allow_credentials=True,allow_methods=['* '],allow_headers=['* ']) 

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('app:app',host="0.0.0.0",port=8000,log_level="info",reload=False)

