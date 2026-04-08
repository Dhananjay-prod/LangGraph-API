# AI Support Agent with LangGraph

An autonomous customer support pipeline built using **LangGraph** and **Google Gemini 2.0 Flash**. 

### Features
* **Multi-stage State Management**: Separates intent classification, sentiment analysis, and response generation into discrete nodes.
* **Health-Tech Ready**: Designed to integrate with EHR platforms for automated patient coordination.
* **Deterministic Scaling**: Uses a compiled state graph to ensure predictable execution flows.

### Setup
1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Add your `GOOGLE_API_KEY` to a `.env` file.
3. Run the agent: `python main.py`
