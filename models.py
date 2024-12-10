def calculate_pricing(village_menu, competitor_prices, weather, busy_times):
    final_prices = {}

    for item, base_price in village_menu.items():
        lowest_price = min(competitor_prices[item])
        if weather["temperature"] < 45 or weather["rain"] or busy_times["Monday"] == "High":
            # Increase price by 10% during busy times or bad weather
            final_prices[item] = lowest_price * 1.10
        else:
            # Set to lowest competitive price
            final_prices[item] = lowest_price

    return final_prices
