from fastapi import FastAPI
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.analyzer import analyze_letters

app = FastAPI()

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_emotion(request: AnalyzeRequest):
    emotions, most_frequent_mood = await analyze_letters(request.letters)
    return AnalyzeResponse(
        emotions=emotions,
        most_frequent_mood=most_frequent_mood
    )
