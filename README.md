# 📉 Amazon Price Tracker

This is a simple Python script that monitors the price of a product on Amazon and sends you an email alert when the price drops below a defined threshold.

---

## 🚀 Features

- Scrapes product title and price from a specific Amazon URL using `BeautifulSoup`
- Sends an email notification if the price drops below `$100`
- Uses environment variables to securely manage sensitive information (email & password)
