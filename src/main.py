from fastapi import FastAPI, Depends, HTTPException, Request, status, Header, Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
#
from .utils import get_env_variable


# Create the FastAPI app
app = FastAPI()
# Add session middleware
SESSION_MIDDLEWARE_KEY= get_env_variable("SESSION_MIDDLEWARE_KEY")
app.add_middleware(SessionMiddleware, secret_key=SESSION_MIDDLEWARE_KEY)

# Example protected endpoint
@app.get("/hello")
async def hello():
    return {"message": "Welcome to the session prototype"}


@app.get("/set/")
async def set_session(request: Request):
    request.session['favourite_colour'] = 'green'
    return {"message": "Session set!"}


@app.get("/get/")
async def get_session(request: Request):
    value = request.session.get('favourite_colour', 'no favourite colour set')
    return {"favourite_colour": value}

