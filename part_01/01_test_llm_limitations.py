# Test pure LLM limitations before applying RAG
import ollama

# Ask Ollama for recent information
response = ollama.chat(
    model='llama3.1:8b',
    messages=[{
        'role': 'user',
        'content': 'What was Apple\'s total revenue in 2023? Please provide the exact number.'
    }]
)

print("LLM Response without RAG:")
print(response['message']['content'])
# Expected result: "I don't have access to 2023 data..."