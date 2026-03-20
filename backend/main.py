import os
import random
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from database import init_db, add_quote, get_all_quotes, delete_quote
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_QUOTES = [
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "The best error message is the one that never shows up.",
    "Simplicity is the soul of efficiency.",
    "Make it work, make it right, make it fast.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "Programming isn't about what you know; it's about what you can figure out.",
    "The only way to learn a new programming language is by writing programs in it.",
    "Sometimes it's better to leave something alone, than to remake it.",
    "The only way to do great work is to love what you do.",
    "Friendship is born at that moment when one person says to another: 'What! You too? I thought I was the only one.'",
    "Love is not about possession. Love is about appreciation.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "True friendship comes when the silence between two people is comfortable."
]

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = None

if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-pro")
    except Exception:
        model = None


class Quote(BaseModel):
    id: int | None = None
    text: str
    created_at: str | None = None


@app.on_event("startup")
def startup():
    init_db()


@app.post("/generate")
def generate_quote():
    try:
        if model:
            categories = ["software development", "motivation", "love", "friendship"]
            category = random.choice(categories)
            prompt = f"Generate a short insightful quote about {category}."
            response = model.generate_content(prompt)
            quote_text = response.text.strip()
        else:
            quote_text = random.choice(TEMP_QUOTES)
        
        quote_id = add_quote(quote_text)
        
        return {
            "id": quote_id,
            "text": quote_text,
            "created_at": datetime.now().isoformat()
        }
    except Exception as e:
        quote_text = random.choice(TEMP_QUOTES)
        quote_id = add_quote(quote_text)
        return {
            "id": quote_id,
            "text": quote_text,
            "created_at": datetime.now().isoformat()
        }


@app.get("/quotes")
def get_quotes():
    return get_all_quotes()


@app.delete("/quote/{quote_id}")
def delete_quote_endpoint(quote_id: int):
    success = delete_quote(quote_id)
    if not success:
        raise HTTPException(status_code=404, detail="Quote not found")
    return {"message": "Quote deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
