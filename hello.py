import requests

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    if request.args.get('state') != "test":
        return render_template('test.html')

    if request.args.get('state') != "authenticated":
        return redirect("https://webexapis.com/v1/authorize?client_id=C7d5cbb55341ea8a2b6a9c8d01ac5534175955483f1a7b1fff528878b4e9016b3&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000&scope=meeting%3Arecordings_read%20spark%3Akms&state=authenticated")
    response = requests.post(
        "https://webexapis.com/v1/access_token",
        {
            "grant_type": "authorization_code",
            "client_id": "C7d5cbb55341ea8a2b6a9c8d01ac5534175955483f1a7b1fff528878b4e9016b3",
            "client_secret": "64e5c0649f266ee6111d720be5a61e580fa022fc7de7d804a5db47beb5a232b9",
            "code": request.args.get('code'),
            "redirect_uri": "http://127.0.0.1:5000"
        }
    )
    token = response.json()['access_token']
    response = requests.get("https://webexapis.com/v1/recordings", headers={'Authorization': 'Bearer:' + token})
    
    return render_template('index.html')