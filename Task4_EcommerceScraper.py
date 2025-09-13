import requests
from bs4 import BeautifulSoup
import csv

# Demo website
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# CSV file create
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Title", "Price", "Rating"])

    # Loop through all books
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]   # rating text hota hai (e.g. "Three")

        writer.writerow([title, price, rating])
        print(f"Book: {title} | Price: {price} | Rating: {rating}")

print("\n✅ Data extracted and saved in books.csv")
