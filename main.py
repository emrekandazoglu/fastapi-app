
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'emre'}}

@app.get('/about')
def about():
    return {'data':['about page',1,2]}