from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from dotenv import load_dotenv
import os

load_dotenv()
config = Config('.env')
oauth = OAuth(config)

salesforce = oauth.register(
    name='salesforce',
    client_id=os.getenv('SALESFORCE_CLIENT_ID'),
    client_secret=os.getenv('SALESFORCE_CLIENT_SECRET'),
    access_token_url='https://login.salesforce.com/services/oauth2/token',
    authorize_url='https://login.salesforce.com/services/oauth2/authorize',
    api_base_url='https://login.salesforce.com/services/data/v56.0/',
    client_kwargs={'scope': 'full refresh_token'}
)

salesforce_router = APIRouter()

@salesforce_router.get("")
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.salesforce.authorize_redirect(request, redirect_uri)

@salesforce_router.get("/callback")
async def auth_callback(request: Request):
    token = await oauth.salesforce.authorize_access_token(request)
    user = token.get('userinfo')
    return {"user": user}