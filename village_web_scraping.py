import requests
from bs4 import BeautifulSoup

def scrape_village_data():
    url = "https://www.yelp.com/biz/village-the-soul-of-india-hicksville"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Scrape basic details
    name = soup.find("h1").text.strip()
    address = soup.find("address").text.strip()
    timings = [time.text.strip() for time in soup.find_all("p", class_="text-size--large__373c0__3t60B")]

    # Return data as a dictionary
    return {"name": name, "address": address, "timings": timings}
