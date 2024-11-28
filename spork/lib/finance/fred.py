from fredapi import Fred
import os

# Set up your FRED API key
API_KEY = "your_fred_api_key_here"  # Replace with your actual API key
fred = Fred(api_key=API_KEY)


def get_unemployment_rate():
    try:
        # Get the data series for unemployment rate (series ID: 'UNRATE')
        data = fred.get_series_latest_release('UNRATE')
        latest_date = data.index[-1]
        latest_value = data.iloc[-1]
        return f"The latest U.S. unemployment rate (as of {latest_date}) is {latest_value}%."
    except Exception as e:
        return f"Error fetching data: {e}"

