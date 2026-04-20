import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES=["USD", "EUR", "INR", "GBP", "JPY"]

def convert_currency(base):
    currencies=",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response=requests.get(url)
        data=response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None
while True:   
    base= input("Enter the base currency (q for quit): ").upper()   
    if base == "Q":
        break 
    amount= input("Enter amount: ")

    try:
        amount=float(amount)
    except:
        print("Invalid amount. ")
        continue

   
    
    data =convert_currency(base)

    if not data:
        continue
    del data[base]

    print(f"\n {amount}{base} equals: \n")
    for ticker, value in data.items():
        converted=amount*value
        print(f"{ticker}: {converted:.2f}")