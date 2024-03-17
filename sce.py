

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



# Function to execute at 10:00 AM
def my_function():
    print("Executing function at 10:00 AM")

# Schedule the function to run at 10:00 AM
schedule.every().day.at("16:55").do(my_function)

# Main loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)



# def send_email(body):
#     sender_email = "akashemail707@gmail.com"
#     receiver_email = "akash7000a@gmail.com"
#     password = "jzzg djgs jwzc daeh"
#     server=smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, password)
#     print("login successful")
#     server.sendmail(sender_email, receiver_email,body)
#     server.quit()

# def geeks():
#     print("enter in geeks")
#     message = "Moving average crossover detected for Buy signal!"
#     send_email(f"Moving Average Crossover Alert, {message}")

# import datetime

# t = st.text_input('time', '9:20')
# st.write('Alarm is set for', t)

# schedule.every().day.at(t).do(geeks)  # Schedule the task to start at the specified tim
# schedule.run_all()

# def main():
#     st.title("Automated Email Sender")
