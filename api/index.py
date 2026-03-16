from fastapi import FastAPI, Request
import google.generativeai as genai
import os

app = FastAPI()

# This connects to the 'Value' you saved in Vercel
api_key = os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY")

@app.post("/api/py/index")
async def travel_planner(request: Request):
    try:
        # 1. Check if the key exists
        if not api_key:
            return {"message": "Error: API Key is missing in Vercel Settings!"}

        # 2. Setup Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        # 3. Get User Input
        data = await request.json()
        user_text = data.get("text", "Paris")
        
        # 4. Ask Gemini
        prompt = f"Give me a 3-bullet point travel itinerary for: {user_text}"
        response = model.generate_content(prompt)
        
        return {"message": response.text}
        
    except Exception as e:
        # This will tell us the EXACT error on the screen
        return {"message": f"Python Error: {str(e)}"}
