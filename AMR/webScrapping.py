
import requests
from bs4 import BeautifulSoup
import pandas

web_url = "https://www.pchotels.com/hotel-and-resort/pearl-continental-hotel-karachi"
response = requests.get(web_url)
print(response)


get_data = BeautifulSoup(response.text, "html.parser")
get_div = get_data.find_all("div", class_="accomodation-content-bx")

get_h3 = get_data.find_all("h3")
RoomName,RoomDescription = [],[]

for data in get_div:
    h3_lao = data.find_all("h3")
    p_lao = data.find_all("p")
    for a in h3_lao:
        RoomName.append(a.text)
    for p in p_lao:
        RoomDescription.append(p.text)

room_data = {
    "RoomName" : RoomName,
    "RoomDescription" : RoomDescription
}

df = pandas.DataFrame(room_data)
print(df)
df.to_csv("room-data.csv",index = False)
