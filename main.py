from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

# URL = "https://appbrewery.github.io/instant_pot/"

URL= "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(url= URL, headers= header)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

# price_dollars = soup.find("span", class_ = "a-price-whole")
# price_cents = soup.find("span", class_ = "a-price-fraction")
#
# print(f"{price_dollars.getText()}{price_cents.getText()}")

price = (soup.find("span", class_= "a-offscreen").getText())
# print(price.split("$")[1])
price_float = float(price.split("$")[1])
message = f"price is reduced, new price {price}"



target_price = 100

load_dotenv()

if price_float < target_price:
    # with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=os.getenv("EMAIL_ADDRESS"), password= os.getenv("EMAIL_PASSWORD"))
    #     connection.sendmail(from_addr= os.getenv("EMAIL_ADDRESS"),
    #                         to_addrs="ajayvarmaj92@gmail.com",
    #                         msg=f"Subject: Friday Motivation\n\n{message}"
    #                         )
    print(f"{message}")