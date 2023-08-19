from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'tan nhat'}}

@app.get('/about')
def about():
    return {'data': 'about page'}

if __name__ == '__main__':
    