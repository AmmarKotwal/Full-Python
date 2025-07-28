import requests
from bs4 import BeautifulSoup
import pandas

web_url = "https://luckyone.com.pk/shopping/"
response = requests.get(web_url)
print(response)

get_data = BeautifulSoup(response.text, "html.parser")
