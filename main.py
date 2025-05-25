from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
}

web_page = requests.get(AMAZON_URL, headers=headers).text
soup = BeautifulSoup(web_page, "html.parser")
price = float(soup.find(class_="a-offscreen").getText().split('$')[1])
title = soup.select(selector="#productTitle")[0].getText()
clean_title = " ".join(title.split())
print(soup.prettify())

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs="fatemepourseif1378@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{clean_title} is now ${price}\n{AMAZON_URL}".encode("utf-8")
        )
