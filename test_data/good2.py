import requests

r = requests.post(
    "http://icanhazip.com",
    data={'foo': 'bar'},
    timeout=10
)
