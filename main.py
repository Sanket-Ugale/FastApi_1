from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return "hey"

@app.get('/about')
def about():
    return "about"