from ollama import Client

_ollama_client = None

def get_llm_client():
    global _ollama_client    
    if _ollama_client is None:
        print("Initializing LLM client...")
        _ollama_client = Client(host='http://localhost:11434')
    return _ollama_client