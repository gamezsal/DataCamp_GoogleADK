from google.adk.agents import Agent
from google.genai import types # For further configuration controls

# In every file, you need to define root_agent - This is important!
root_agent = Agent(

    name = "welcome_agent", # Name of our AI Agent 
    model = "gemini-2.0-flash", # Underlying Model we will be using
    description = "Greeting Agent", # A brief description of the agent 
    instruction = "You are an enthusiastic expert on the Google ADK (Agent Development Kit). You greet users warmly, use emojis 🚀, and offer to help them navigate the tutorial and build amazing agents. You are friendly, encouraging, and concise.", # Detailed things the Agent has to do

    generate_content_config=types.GenerateContentConfig(
        temperature=0.7, # Higher temperature for more creative and varied responses
        max_output_tokens=250
    )
)

