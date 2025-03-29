from datetime import datetime, timezone
#
from fastapi import FastAPI, Depends, HTTPException, Request, status, Header, Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
#
from .utils import get_env_variable, get_local_dt_iso_with_tz_info


# Create the FastAPI app
app = FastAPI()
# Add session middleware
SESSION_MIDDLEWARE_KEY= get_env_variable("SESSION_MIDDLEWARE_KEY")
app.add_middleware( SessionMiddleware, 
                    secret_key=SESSION_MIDDLEWARE_KEY,
                    session_cookie="session_prototype",
                    max_age=None,
                    same_site='strict')
#
#

@app.get("/set/")
async def set_session(request: Request):

    local_dt_iso_with_tz_info=get_local_dt_iso_with_tz_info()
    #
    request.session['favourite_colour'] = 'green'
    request.session['favourite_colour_last_changed'] = local_dt_iso_with_tz_info
    #
    return {"message": "Session set!"}


@app.get("/get/")
async def get_session(request: Request):
    colour = request.session.get('favourite_colour', 'no favourite colour set')
    colour_last_change  = request.session.get('favourite_colour_last_changed', 'no date of previous update for favourite colour')
    return {"favourite_colour": colour, "last_update_time": colour_last_change}


# Placeholder endpoint
@app.get("/")
async def hello():
    return {"message": "Welcome to the session prototype"}

