from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from dotenv import load_dotenv
import os

load_dotenv()
config = Config('.env')
oauth = OAuth(config)

facebook = oauth.register(
    name='facebook',
    client_id=os.getenv('FACEBOOK_CLIENT_ID'),
    client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
    access_token_url='https://graph.facebook.com/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    api_base_url='https://graph.facebook.com/v12.0/',
    client_kwargs={'scope': 'email'}
)

facebook_router = APIRouter()

@facebook_router.get("")
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.facebook.authorize_redirect(request, redirect_uri)

@facebook_router.get("/callback")
async def auth_callback(request: Request):
    token = await oauth.facebook.authorize_access_token(request)
    user = token.get('userinfo')
    return {"user": user}