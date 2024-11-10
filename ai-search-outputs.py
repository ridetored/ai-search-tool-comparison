import requests
import csv
import datetime
# Define your API endpoints and keys for the AI tools
API_DETAILS = {
    'ChatGPT': {'API_ENDPOINT': 'https://api.openai.com/v1/engines/chatgpt/completions', 'API_KEY': 'your_chatgpt_api_key'},
    'Google Bard': {'API_ENDPOINT': 'https://api.google.com/bard', 'API_KEY': 'your_google_bard_api_key'},
    'Perplexity AI': {'API_ENDPOINT': 'https://api.perplexity.ai/query', 'API_KEY': 'your_perplexity_api_key'}
}
# Function to get AI response
def get_ai_response(tool_name, query):
    api_info = API_DETAILS[tool_name]
    headers = {"Authorization": f"Bearer {api_info['API_KEY']}"}
    data = {"prompt": query, "max_tokens": 100}  # Modify as per tool's API requirements
    response = requests.post(api_info['API_ENDPOINT'], headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('choices', [{}])[0].get('text', 'No response')
    else:
        return f"Error {response.status_code}: {response.text}"
# Test queries
queries = ["What is the best AI search engine?", "How does AI improve search results?"]
# Write responses to CSV
with open('ai_search_outputs.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tool', 'Query', 'Response', 'Date'])
    for tool in API_DETAILS.keys():
        for query in queries:
            response = get_ai_response(tool, query)
            writer.writerow([tool, query, response, datetime.datetime.now().isoformat()])
print("Responses saved to ai_search_outputs.csv")
