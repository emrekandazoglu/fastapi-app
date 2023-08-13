
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished') # we have to put static route above dynamic route
def unpublished():
    #fetch blog with id=id
    return {'data':'unpublished'}

@app.get('/blog/{id}')
def show(id: int): # we changed type of id
    #fetch blog with id=id
    return {'data':id}



@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id=id
    return  {'data':{'1':'hello','2':'hello'}}