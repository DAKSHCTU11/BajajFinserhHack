<<<<<<< HEAD
# BajajFinserhHack
FAST API CODE
=======
# BFHL API (Bajaj Finserv Hackathon)

## 🚀 Overview
This is a REST API built with **FastAPI** as part of the Bajaj Finserv Hackathon.  
It processes an input array and returns categorized outputs including numbers, alphabets, special characters, and summary statistics.

---

## 🔧 Endpoint
**POST** `/bfhl`

### ✅ Request Example
```json
{
  "data": ["a","1","334","4","R","$"]
}

Response Example

{
  "is_success": true,
  "user_id": "daksh_chaudhary_22052003",
  "email": "dakshctu11@gmail.com",
  "roll_number": "22bit0511",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
>>>>>>> a51e862 (Initial commit - BFHL API)
