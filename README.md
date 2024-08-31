# Pterodactyl Tools

Tools I've wrote to interact with my Pterodactyl server. API docs: https://dashflo.net/docs/api/pterodactyl/v1/

Current tools:
- Console Reader - Authenticates with the clients API to get a token and websocket URL, connects to the websocket and prints received messages. Planning on writing an integration for Zabbix. Need to handle re-authenticating when token expires.
