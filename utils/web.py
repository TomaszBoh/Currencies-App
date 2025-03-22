import requests
import json
from datetime import datetime

def make_query_url(year, month, day, table="A"):
    return f"https://api.nbp.pl/api/exchangerates/tables/{table}/{year:04}-{month:02}-{day:02}/?format=json"

def gets_rates(year, month, day, table="A", expected_currencies=["eur", "usd", "gbp", "chf"]):

    expected_currencies_lower = [element.lower() for element in expected_currencies]

    query_url = make_query_url(year, month, day, table)
    results = requests.get(query_url)

    if results.status_code !=200:
        return []
    
    table = results.json()[0]
    rates = table.get("rates", [])
    rates_filtered = [ rate for rate in rates
                     if rate["code"].lower() in expected_currencies_lower]
    
    date = datetime(year, month, day).date().strftime("%Y-%m-%d")
    for rate in rates_filtered:
        rate.update({"date": date})

    return rates_filtered