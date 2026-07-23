from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def greeting_u():
    return "Good Morning"

    # OR
    
    # return {'message': 'Good Morning [23-07-2026]'}

@app.get("/about")
def date():
    return "23/07/2026"    