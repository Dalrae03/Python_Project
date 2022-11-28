import requests

url = "https://www.google.com/?hl=ko"
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status