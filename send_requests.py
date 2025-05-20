# formatted for Google colab notebook
#Benchmark script to send requests to the deployed endpoint 'apiLink'
#Returns the json of the response if it is successful, otherwise returns none
import requests
import json

def send_request(apiLink, prompt):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": "/content/TinyLlama-1.1B-Chat-v1.0",  
        "prompt": prompt,
        "max_tokens": 50,
        "temperature": 0.7
    }

    try: # from requests library to send an HTTPS post to the web server (where it is deployed)
        response = requests.post(f"{apiLink}/v1/completions", headers=headers, data=json.dumps(payload), timeout=10)
        if response.status_code == 200: #200 is the code for succesfully received
            return response.json()
        else:
            print(f"Endpoint request failed with code: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
        return None

# Now call the function
apiLink = "http://localhost:8000"   
prompt = "What is the weather like today?"

response = send_request(apiLink, prompt)
if response:
    print("Response received:")
    print(json.dumps(response, indent=2))
else:
    print("Failed to get response from API.")






