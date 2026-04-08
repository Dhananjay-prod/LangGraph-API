import os
from dotenv import load_dotenv
from app import app  # Import your compiled graph

# Load keys from .env
load_dotenv()

def run_support_agent(ticket_text: str):
    initial_state = {
        "ticket": ticket_text,
        "intent": "",
        "sentiment": "",
        "response": ""
    }
    
    print(f"--- Processing Ticket: {ticket_text} ---")
    final_state = app.invoke(initial_state)
    
    print("\n[AI ANALYSIS]")
    print(f"Intent: {final_state['intent']}")
    print(f"Sentiment: {final_state['sentiment']}")
    print(f"\n[GENERATED RESPONSE]\n{final_state['response']}")

if __name__ == "__main__":
    test_ticket = "My order hasn't arrived in 2 weeks and no one is responding."
    run_support_agent(test_ticket)
