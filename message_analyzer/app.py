from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class Item(BaseModel):
    content: str

TAGS = [
    "phone_number_in_first_message",
    "spelled_out_phone_number",
    "suspicious_number_detected",
    "sketchy_contact_information",
    "unicode_detected",
    "url_detected",
    "phone_number_detected",
    "forbidden_words_in_message"
]

# > { "content": "content to detect" }
# => { "clean": true/false, "detected_flags": ["url_detected", "phone_number_detected"] }

@app.post("/analyze")
async def analyze_content(item: Item):
    response = {
        "detected_flags": [],
        "clean": True
    }

    # 1 in 5 chance for 'clean' to be false
    if random.randint(1, 5) == 1:
        response["clean"] = False
        number_of_flags = random.randint(1, 3)
        response["detected_flags"] = random.sample(TAGS, number_of_flags)

    return response
