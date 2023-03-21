from fastapi import  FastAPI, HTTPException , Request 
from fastapi.middleware.cors  import  CORSMiddleware 
from fastapi.responses  import JSONResponse 
from fastapi.exceptions  import  HTTPException
from fastapi import APIRouter,status,Depends,HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from schemas.users_schema import UserSchemaBase
from firebase_admin import auth
from sqlalchemy.future import select
from models.users_model import UserModel
import firebase_admin
import pyrebase
import json

router = APIRouter()

@router.post("/signup",include_in_schema=False)
async def signup(user:UserSchemaBase,db:AsyncSession = Depends(get_session)):

    try:
        user_firebase = auth.create_user(username=user.username,name=user.name,surname=user.surname,email=user.email,password=user.password)

        if user_firebase is not None:
            async with db as session:
                new_user:UserModel = UserModel(name=user.name,surname=user.surname,username=user.username,email=user.email,password=user.password,uid=user.uid)
                
                query = select(UserModel).filter(user.email == UserModel.email)
                result = await session.execute(query)
                email = result.scalars().unique().one_or_none()

                if email:
                    session.add(new_user)
                


            return JSONResponse(content={"message":f"Successfully created user {user.uid}"},status_code=status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="Failed to create firebase user, please review information and try again",status_code=status.HTTP_400_BAD_REQUEST)
        
    except:
        return HTTPException(detail={'message': 'Error Creating User'}, status_code=status.HTTP_400_BAD_REQUEST)

@router.post("/login",include_in_schema=False)
async def login(request:Request):
    req_json = await request.json()
    credentials = {"email":req_json['email'],"password":req_json['password']}

    try:
        cred = credentials.Certificate("metanalysis_service_account_keys.json")
        firebase = firebase_admin.initialize_app(cred)
        pb = pyrebase.initialize_app(json.load(open("firebase_config.json")))

        user = pb.auth().sign_in_with_email_and_password(credentials['email'],credentials['password'])

        jwt = user['idToken']

        if jwt is not None:
            return JSONResponse(content={"access_token":jwt,"token_type":"bearer"},status_code=status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="Incorrect username or password, please try again",status_code=status.HTTP_401_UNAUTHORIZED)
        
    except:
        return JSONResponse(content={'message':'There was an error logging in'},status_code=status.HTTP_400_BAD_REQUEST)
                          
@router.post("/ping",include_in_schema=False)
async def validate(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')
    print(f"jwt:{jwt}")
    user = auth.verify_id_token(jwt)

    return user['uid']
