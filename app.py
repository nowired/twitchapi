from fastapi import FastAPI, Query
import requests
import os

app = FastAPI()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

oauth_token = None

def get_oauth_token():
    global oauth_token
    if oauth_token:
        return oauth_token

    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    oauth_token = response.json()["access_token"]
    return oauth_token

def get_user_about(username: str):
    token = get_oauth_token()
    url = "https://api.twitch.tv/helix/users"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {
        "login": username
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    if data["data"]:
        return data["data"][0]["description"]
    return "No se encontró la descripción."

@app.get("/")
def root():
    return {"message": "Twitch About API"}

@app.get("/about")
def about(user: str = Query(...)):
    try:
        description = get_user_about(user)
        return description or "No hay descripción disponible."
    except Exception as e:
        return f"Error al obtener información: {str(e)}"
