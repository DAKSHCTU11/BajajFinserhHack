from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

# 🎯 Create FastAPI app
app = FastAPI(
    title="BFHL API",
    description="Bajaj Finserv Hackathon Task",
    docs_url="/bfhl",     # 👈 Swagger UI will now be at /bfhl
    redoc_url=None        # (optional) disables ReDoc
)

# 📌 Your identity
FULL_NAME = "daksh_chaudhary"
DOB = "22052003"   # ddmmyyyy
EMAIL = "dakshctu11@gmail.com"
ROLL_NUMBER = "22bit0511"

# 📥 Expected input schema
class InputData(BaseModel):
    data: List[str]

# --- Helper functions ---
def is_number(val: str) -> bool:
    return val.isdigit()

def is_alphabet(val: str) -> bool:
    return val.isalpha()

def split_data(items: List[str]):
    odds, evens, letters, specials = [], [], [], []
    total = 0
    for item in items:
        if is_number(item):
            num = int(item)
            total += num
            (evens if num % 2 == 0 else odds).append(str(num))
        elif is_alphabet(item):
            letters.append(item.upper())
        else:
            specials.append(item)
    return odds, evens, letters, specials, str(total)

def build_funny_concat(letters: List[str]) -> str:
    text = "".join(letters)[::-1]
    return "".join(
        ch.upper() if i % 2 == 0 else ch.lower()
        for i, ch in enumerate(text)
    )

# --- POST API Route ---
@app.post("/bfhl")
async def process_data(payload: InputData):
    try:
        odds, evens, letters, specials, total_sum = split_data(payload.data)
        concat_string = build_funny_concat(letters)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": letters,
            "special_characters": specials,
            "sum": total_sum,
            "concat_string": concat_string
        }
        return response
    except Exception as e:
        return {"is_success": False, "error": str(e)}
