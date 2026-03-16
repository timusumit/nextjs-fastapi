from fastapi import FastAPI, Request
import google.generativeai as genai
import os
@app.post("/api/index")
app = FastAPI()

# Connect to your Google Key
genai.configure(api_key=os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.post("/api/index")
async def travel_planner(request: Request):
    # Get the user's message from the frontend
    data = await request.json()
    user_text = data.get("text", "Paris")
    
    # Ask Gemini to create the plan
    prompt = f"Plan a short trip based on this request: {user_text}. Give me 3 bullet points of what to do."
    response = model.generate_content(prompt)
    
    return {"message": response.text}
