import os
import openai
from collections import Counter
from app.config import OPENAI_API_KEY# .env에서 API 키 가져오기

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_letters(letters: list):
    """최근 5개의 편지를 감정 분석하고, 감정별 통계와 가장 많은 감정 반환"""
    emotion_list = []
   
    try:
        for content in letters:
            if content.emotion:
                emotion_list.append(content.emotion)
                continue

            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "너는 감정을 분석하는 AI야. 사용자가 쓴 여러 편지를 문맥과 단어 등을 고려하여 분석하고 감정을 무조건 happy, sad, angry, worried, neutral 중 하나로 나타내주세요"
                    },
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                max_tokens=7
            )
            emotion = response.choices[0].message.content.strip().lower()
            emotion_list.append(emotion)
    except openai.error.RateLimitError:
            emotion_list.append("neutral") #Rate limit 시 기본값으로 설정정

        
    # 감정 통계
    emotion_counts = dict(Counter(emotion_list))
    most_frequent = max(emotion_counts.items(), key=lambda x: x[1])[0] if emotion_counts else None

    return emotion_counts, most_frequent

