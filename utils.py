from yelpapi import YelpAPI

def get_nearby_restaurants():
    API_KEY = "YOUR_YELP_API_KEY"
    yelp_api = YelpAPI(API_KEY)

    results = yelp_api.search_query(
        term="restaurant",
        location="Hicksville, NY",
        radius=2000,  # 2 km
        sort_by="rating",
        limit=5
    )

    competitors = []
    for business in results["businesses"]:
        competitors.append({
            "name": business["name"],
            "address": business["location"]["address1"],
            "rating": business["rating"]
        })
    
    return competitors


#open weather API
def get_weather():
    API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
    city = "Hicksville"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract relevant details
    temp_kelvin = data["main"]["temp"]
    temperature = (temp_kelvin - 273.15) * 9/5 + 32  # Convert Kelvin to Fahrenheit
    rain = "rain" in data

    return {"temperature": temperature, "rain": rain}
