import requests
import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/')
def generate_token():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }
    data = {
        'partnerUserId': generate_random_string(64)
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            token = response.json()['token']
            return jsonify({'nitro': f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"})
        else:
            return jsonify({"error": f"An error occurred: {response.status_code}"})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)
