import os
import requests
from dotenv import load_dotenv
import websockets
import asyncio
import json

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('ptero_client_key')
server_url = os.getenv('ptero_server_url')
server_id = os.getenv('server_id')

endpoint = f"/api/client/servers/{server_id}/websocket"
url = f"{server_url}{endpoint}"

# Set up the request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Accept": "Application/vnd.pterodactyl.v1+json"
}

response = requests.get(url, headers=headers)
response_json = response.json()

websocket_url = response_json["data"]["socket"]
token = response_json["data"]["token"]

print(token, websocket_url)

# Asynchronous function for connecting to websocket and printing received messages
async def connect_and_authenticate():
    print("Connecting to websocket")
    async with websockets.connect(websocket_url) as websocket:
        print("Connected to websocket")
        auth_message = {
            "event": "auth",
            "args": [token]
        }

        print("\n\n\n", auth_message)
        # Send authentication message
        await websocket.send(json.dumps(auth_message))

        # Print received messages from websocket
        try:
            async for message in websocket:
                print(f"Received: {message}")
        except websockets.ConnectionClosed:
            print("Connection closed.")

asyncio.run(connect_and_authenticate())
