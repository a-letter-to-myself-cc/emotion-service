from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    letters: List[str]

class AnalyzeResponse(BaseModel):
    emotions: dict
    most_frequent_mood: str
