from fastapi import FastAPI  

app = FastAPI()



@app.get("/")
def hello():
    return {'message': 'Hello world'}


@app.get("/about")
def about():
    return {"message": "Hello my name is nikhil"}