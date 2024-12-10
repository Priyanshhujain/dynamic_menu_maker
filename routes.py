from flask import Blueprint, jsonify
from .utils import scrape_village_data, get_nearby_restaurants, get_weather
from .models import calculate_pricing

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/village-data", methods=["GET"])
def village_data():
    data = scrape_village_data()
    return jsonify(data)

@api_routes.route("/pricing", methods=["GET"])
def pricing():
    village_menu = {"Butter Chicken": 12.99, "Naan": 2.99, "Biryani": 14.99}
    competitor_prices = {
        "Butter Chicken": [11.99, 13.99],
        "Naan": [2.49, 3.00],
        "Biryani": [13.49, 15.99]
    }
    weather = get_weather()
    busy_times = {"Monday": "High"}

    final_prices = calculate_pricing(village_menu, competitor_prices, weather, busy_times)
    return jsonify({"final_prices": final_prices})
