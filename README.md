# dynamic_menu_maker
# 📈 Dynamic Pricing API for Restaurants

This project is a **dynamic pricing algorithm** designed to optimize restaurant menu prices in real time. It adjusts prices based on local competition, weather conditions, and busy times. Built with **Python** and **Flask**, the API integrates multiple data sources to provide intelligent, data-driven pricing recommendations.

---

## 📝 **Table of Contents**
1. [Problem Statement](#problem-statement)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Folder Structure](#project-folder-structure)
5. [Installation and Setup](#installation-and-setup)
6. [API Endpoints](#api-endpoints)
7. [Example Usage](#example-usage)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## 📌 **Problem Statement**
The goal is to create an **ML-driven pricing algorithm** for a restaurant named **Village**. The algorithm dynamically sets menu prices by analyzing the following factors:
- **Local competitor prices** (via Yelp)
- **Weather conditions** (via OpenWeatherMap)
- **Busy times** (via Google Maps)  

This enables the restaurant to make **real-time price adjustments** that maximize profitability.

---

## 🚀 **Features**
- **Restaurant Data Scraping**: Extracts menu, pricing, and operating hours for the restaurant.  
- **Competitor Analysis**: Identifies nearby competitor restaurants and their menu prices.  
- **Weather Integration**: Tracks weather conditions to adjust prices during harsh weather.  
- **Busy Times Analysis**: Uses Google Maps data to analyze peak times and adjust prices accordingly.  
- **Dynamic Pricing**: Updates menu prices in real time using a machine learning model.  

---

## ⚙️ **Technology Stack**
**Backend**  
- **Flask**: For API endpoints and server.  
- **BeautifulSoup**: For web scraping restaurant details from Yelp.  
- **Requests**: To communicate with external APIs (Yelp, OpenWeatherMap, Google Maps).  

**Machine Learning**  
- **Scikit-Learn**: Builds a simple pricing model.  
- **Pandas & NumPy**: Handles data manipulation and analysis.  

**Deployment**  
- **Gunicorn**: Runs the Flask app in production.  
- **Heroku**: Deploys the API online.  

---

## 📁 **Project Folder Structure**

**project/** 
**├── app/ │**
                  **├── init.py # Flask app initialization │**
                  **├── routes.py # API endpoints for Village data and pricing │**
                  **├── utils.py # Utility functions for web scraping and API calls │ **
                  **├── models.py # Pricing algorithm logic **
                  **├── run.py # Main entry point for running the application** 
├── requirements.txt # List of dependencies**
├── README.md # Project documentation
