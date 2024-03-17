

import streamlit as st

import smtplib
import schedule
import time

st.set_page_config(
    page_title='Akash',
    layout='wide'
)

# tab1, tab2, tab3 = st.tabs(["Nifty 100", "Banking" , "Agriculture", "Automobile"])

# with tab1:
dg='hdfc-bank-ltd'
st.markdown(f'[Click here to go to another page](https://groww.in/charts/stocks/{dg}?exchange=NSE)')

def send_email(body):
    sender_email = "akashemail707@gmail.com"
    receiver_email = "akash7000a@gmail.com"
    password = "jzzg djgs jwzc daeh"
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    print("login successful")
    server.sendmail(sender_email, receiver_email,body)
    server.quit()

def geeks():
    print("enter in geeks")
    message = "Moving average crossover detected for Buy signal!"
    send_email(f"Moving Average Crossover Alert, {message}")


def start_scheduling(start_time):
    schedule.every().day.at(start_time).do(geeks)  # Schedule the task to start at the specified time
    print(f"Scheduling started at {start_time}")

# Function to stop scheduling
def stop_scheduling(stop_time):
    schedule.clear()  # Clear all scheduled tasks
    print(f"Scheduling stopped at {stop_time}")

# # Main function
# if __name__ == "__main__":
#     start_time = "14:11"  # Specify the start time
#     stop_time = "14:13"   # Specify the stop time
    
#     start_scheduling(start_time)
    
#     # Keep the program running until the stop time is reached
#     while True:
#         current_time = time.strftime("%H:%M", time.localtime())
#         if current_time >= stop_time:
#             stop_scheduling(current_time)
#             break
#         schedule.run_pending()
#         time.sleep(1)
 
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
