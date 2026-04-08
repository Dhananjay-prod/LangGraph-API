from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
import operator

class TicketState(TypedDict):
    ticket: str
    intent: str
    sentiment: str
    response: str

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def classify_intent(state: TicketState) -> dict:
    result = llm.invoke(f"Classify intent in one word: {state['ticket']}")
    return {"intent": result.content.strip()}

def analyze_sentiment(state: TicketState) -> dict:
    result = llm.invoke(f"Classify sentiment as positive/neutral/negative: {state['ticket']}")
    return {"sentiment": result.content.strip()}

def generate_response(state: TicketState) -> dict:
    prompt = f"Ticket: {state['ticket']}\nIntent: {state['intent']}\nSentiment: {state['sentiment']}\nWrite a helpful support response:"
    result = llm.invoke(prompt)
    return {"response": result.content.strip()}

graph = StateGraph(TicketState)
graph.add_node("classify_intent", classify_intent)
graph.add_node("analyze_sentiment", analyze_sentiment)
graph.add_node("generate_response", generate_response)

graph.set_entry_point("classify_intent")
graph.add_edge("classify_intent", "analyze_sentiment")
graph.add_edge("analyze_sentiment", "generate_response")
graph.add_edge("generate_response", END)

app = graph.compile()

result = app.invoke({"ticket": "My order hasn't arrived in 2 weeks and no one is responding.", "intent": "", "sentiment": "", "response": ""})
print(result["response"])
