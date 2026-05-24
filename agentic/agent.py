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

#after this (pip install -r requirements.txt)



load_dotenv()

MODEL = "gemini-2.5-flash"

def tell_pm(country : str) -> str:
    COUNTRY_PM_TOOL = {
        "India": "Narendra Modi",
        "United Kingdom": "Rishi Sunak",
        "Canada": "Justin Trudeau",
        "Australia": "Anthony Albanese",
        "New Zealand": "Christopher Luxon"
    }
     
    return COUNTRY_PM_TOOL.get(country, "sorry I don't know")

root_agent = LlmAgent(
    model=MODEL,
    name="travel_coordinator",
    description=(
        "You are an agents that tells prime minister of different countries"
    ),
    instruction="""
    You are a friendly agent that tells prime minister of different countries. Use tool tell_pm first to find the PM and if it does not contain info use your own brain.

    for greetings return normal response.

    """,
    tools=[tell_pm]
    
)

# root_agent = LlmAgent(
#     model=MODEL,
#     name="travel_coordinator",
#     description=(
#         "You are an agents that tells prime minister of different countries"
#     ),
#     instruction="""
#     You are a friendly agent that tells prime minister of different countries. 

#     for greetings return normal response.

#     """
    
# )
    