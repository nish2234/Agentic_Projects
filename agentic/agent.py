import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent

#How to activate venv

# Create a virtual environment named 'venv'
#python -m venv venv

# Windows (Command Prompt)
#venv\Scripts\activate

# Windows (PowerShell)
#venv\Scripts\Activate.ps1

# Linux / macOS
#source venv/bin/activate



load_dotenv()

MODEL = "gemini-2.5-flash"


root_agent = LlmAgent(
    model=MODEL,
    name="travel_coordinator",
    description=(
        "Main travel assistant that coordinates trip planning, "
        "flight search, and hotel search."
    ),
    instruction="""You are a friendly travel coordinator managing a team of 3 specialists.

                When a user asks to plan a trip:
                1. FIRST delegate to 'trip_planner' to create the itinerary.
                2. THEN delegate to 'flight_search' to find real flight options.
                3. THEN delegate to 'hotel_search' to find real hotel options.


                For simple greetings or non-travel questions, respond directly and politely.
                Always be enthusiastic about travel!""",
    
)