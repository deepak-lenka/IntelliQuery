from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from data import vector_db_data
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Query(BaseModel):
    text: str

class VectorDB:
    def __init__(self, data):
        self.data = data
    
    def query(self, text):
        for key, value in self.data.items():
            if all(word in text.lower() for word in key.lower().split()):
                return value
        return "No information found in the database."

vector_db = VectorDB(vector_db_data)

def should_use_vectordb(query):
    question_words = ["what", "where", "who", "when", "which", "how"]
    return any(query.lower().startswith(word) for word in question_words)

def generate_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don't eggs tell jokes? They'd crack each other up!",
    ]
    return random.choice(jokes)

def generate_fun_fact():
    fun_facts = [
        "The shortest war in history lasted 38 minutes.",
        "A group of flamingos is called a 'flamboyance'.",
        "The first oranges weren't orange.",
        "The Eiffel Tower can be 15 cm taller during the summer.",
        "Octopuses have three hearts.",
    ]
    return random.choice(fun_facts)

def process_query(text):
    text = text.lower()
    if text in ["hello", "hi", "hey"]:
        return "Hello! How can I assist you today? I can answer questions, tell jokes, or share fun facts!"
    elif "joke" in text:
        return f"Here's a joke for you: {generate_joke()}"
    elif "fun fact" in text or "interesting fact" in text:
        return f"Here's an interesting fact: {generate_fun_fact()}"
    elif should_use_vectordb(text):
        return vector_db.query(text)
    else:
        return "I'm not sure how to respond to that. Can you ask a question, request a joke, or ask for a fun fact?"

@app.post("/query")
async def query_endpoint(query: Query):
    response = process_query(query.text)
    return JSONResponse(content={"response": response})

@app.post("/agent")
async def agent_endpoint(query: Query):
    response = process_query(query.text)
    return JSONResponse(content={"response": response})

@app.get("/")
async def serve_html():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)