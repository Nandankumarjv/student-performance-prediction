from fastapi import fastapi

app=FastAPI()

@app.get('/')
def details():
    return {
        "This is a sample message..."
    }