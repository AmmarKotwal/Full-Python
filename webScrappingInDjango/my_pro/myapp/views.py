from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd

def web(request):
    # Target URL
    web_url = "https://propakistani.pk/category/others/education/"
    response = requests.get(web_url)
    response.encoding = 'utf-8'  # ensure proper text encoding

    # Parse HTML
    get_data = BeautifulSoup(response.text, "html.parser")

    # Each article block is inside <article> tag
    articles = get_data.find_all("article")

    BlogTitles, BlogLinks, BlogDescriptions = [], [], []

    for article in articles:
        # Extract title and link
        title_tag = article.find("h2", class_="post-box-title")
        if title_tag and title_tag.find("a"):
            BlogTitles.append(title_tag.text.strip())
            BlogLinks.append(title_tag.find("a")["href"])
        else:
            BlogTitles.append("No title")
            BlogLinks.append("#")

        # Extract description paragraph
        desc_tag = article.find("p")
        if desc_tag:
            BlogDescriptions.append(desc_tag.text.strip())
        else:
            BlogDescriptions.append("No description available")

    # Combine into a single structure
    blog_data = zip(BlogTitles, BlogLinks, BlogDescriptions)

    # Optional: Save to CSV
    df = pd.DataFrame({
        "Title": BlogTitles,
        "Link": BlogLinks,
        "Description": BlogDescriptions
    })
    df.to_csv("education_blogs.csv", index=False)

    # Render in HTML
    return render(request, "myapp/webForScrap.html", {"blog_data": blog_data})

