# Using Sessions in FastAPI
A project to experiment with the use of sessions from within FastAPI by using the Starlette middleware -  https://www.starlette.io/middleware/#sessionmiddleware .

The aim here is to replicate parts of the functionality of the Django Sessions facility, as it says in the [Django Sessions doco](https://docs.djangoproject.com/en/5.1/topics/http/sessions/) - _"The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the sending and receiving of cookies."_.

## Starting the server
### VirtualEnv Initialization
From the root of the project execute ...

```
$ pipenv shell
```

### Start Server
From the root of the project execute ...
```
uvicorn src.main:app --reload
```

