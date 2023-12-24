import requests
import csv

API_KEY = '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'
API_URL = 'https://api.openai.com/v1/completions'

def fetch_chatgpt_answer(question):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    payload = {
        'model': 'text-davinci-003',
        'prompt': question,
        'max_tokens': 4000,
        'temperature': 1.0
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_csv(data):
    with open('chatgpt_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['question', 'answer'])
        writer.writerow(data)

# Example usage:
if __name__ == "__main__":
    question = "What is gluten sensitivity?"
    result = fetch_chatgpt_answer(question)

    if result:
        answer = result['choices'][0]['text']
        data = {'question': question, 'answer': answer}
        save_to_csv(data)
        print("Réponse enregistrée dans le fichier CSV.")
    else:
        print("Échec de la récupération de la réponse.")
