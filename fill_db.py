import requests

request = requests.get("http://nova-hub.ru:9999/moc/cards_1")
print(request.json())
