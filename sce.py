# import yfinance as yf
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
import schedule
import time
import streamlit as st

st.write("gello")
def geeks():
    print("Shaurya says Geeksforgeeks")
 
# # Task scheduling
# # After every 10mins geeks() is called. 
# schedule.every(1).minutes.do(geeks)
# while True:
 
#     # Checks whether a scheduled task 
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)

# # Function to send email
# def send_email(subject, body):
#     sender_email = "your_email@example.com"
#     receiver_email = "recipient_email@example.com"
#     password = "your_email_password"

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.example.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         text = message.as_string()
#         server.sendmail(sender_email, receiver_email, text)

# # Function to check moving average crossover
# def check_crossover(symbol, short_window=50, long_window=200):
#     data = yf.download(symbol, start="2023-01-01", end="2024-01-01") # Adjust date range as needed
#     data["Short_MA"] = data["Close"].rolling(window=short_window).mean()
#     data["Long_MA"] = data["Close"].rolling(window=long_window).mean()

#     if data["Short_MA"].iloc[-2] < data["Long_MA"].iloc[-2] and data["Short_MA"].iloc[-1] > data["Long_MA"].iloc[-1]:
#         message = f"Moving average crossover detected for {symbol}. Buy signal!"
#         send_email("Moving Average Crossover Alert", message)

# def schedule_crossover_check():
#     # Schedule the crossover check to run every 5 minutes after 10:00 AM
#     schedule.every(5).minutes.after("10:00").do(check_crossover, symbol="AAPL")  # Subsequent runs every 5 minutes

# # Function to cancel scheduling after 3:00 PM
# def stop_scheduling():
#     schedule.clear()

# # Main loop to run the scheduler
# if __name__ == "__main__":
#     schedule_crossover_check()
#     schedule.every().day.at("15:00").do(stop_scheduling)  # Schedule to stop scheduling at 3:00 PM
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
