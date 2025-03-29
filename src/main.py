from fastapi import FastAPI, Depends, HTTPException, Request, status, Header, Cookie
from fastapi.responses import RedirectResponse, HTMLResponse

###################################################################################
def get_env_variable(var_name):
    """Get the env var value or throw an exception"""
    try:
        return os.environ[var_name]
    except KeyError as e:
        e.add_note("Set the %s environment variable" % var_name)
        raise

# Create the FastAPI app
app = FastAPI()

# Example protected endpoint
@app.get("/hello")
async def hello():
    return {"message": "Welcome to the session prototype"}
