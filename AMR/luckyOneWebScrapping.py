import pandas
import requests
from bs4 import BeautifulSoup
web_url = "https://www.nueplex.com/ticket.html"
response = requests.get(web_url)
print(response)
data_uthao = BeautifulSoup(response.text,"html.parser")
table_lao = data_uthao.find_all("div",class_="table-responsive ticket")
print(table_lao)
moviename,price=[],[]
for data in table_lao:
    table= data.find_all("table",class_="table")
    for tr in table:
        tbody_lao=data.find_all("tbody")

        for tr in tbody_lao:
            tr= data.find_all("tr")
            for th_lao in tr:
                th= data.find_all("th")
                td=data.find_all("td")
                for th_lao in th:
                    moviename.append(th_lao.text)
        # for td_lao in td:
        #     price.append(td_lao.text)

Movies_data = {
"Movie Name":moviename,
# "Price":price
}
movie_df = pandas.DataFrame(Movies_data)
print(movie_df)