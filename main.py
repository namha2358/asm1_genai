# main.py
from fastapi import FastAPI    # import the FastAPI web framework

app = FastAPI()                # create the application object that will hold all our endpoints

@app.get("/")                  # register a GET endpoint at the root URL "/"
def read_root():               # this function runs whenever someone visits "/"
    return {"message": "Hello, FastAPI with UV!"}   # FastAPI converts this dict to JSON automatically