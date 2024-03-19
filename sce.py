

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


col1,col2=st.columns(2)



# def send_email(body):
#     sender_email = "akashemail707@gmail.com"
#     receiver_email = "akash7000a@gmail.com"
#     password = "jzzg djgs jwzc daeh"
#     server=smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, password)
#     st.write("login successful")
#     server.sendmail(sender_email, receiver_email,body)
#     server.quit()

# def task():
#     mess="Performing the task..."
#     send_email(mess)

# # Function to start scheduling
# def start_scheduling(start_time):
#     schedule.every().day.at(start_time).do(task)  # Schedule the task to start at the specified time
#     st.write(f"Scheduling started at {start_time}")

# # Function to stop scheduling
# def stop_scheduling(stop_time):
#     schedule.clear()  # Clear all scheduled tasks
#     st.write(f"Scheduling stopped at {stop_time}")


# start_time = st.text_input('start_time', '09:15') 
# stop_time = st.text_input('stop_time', '09:16')


# if st.button('Say hello'):
#     start_scheduling(start_time)
#     while True:
#         current_time = time.strftime("%H:%M", time.localtime())
#         if current_time >= stop_time:
#             stop_scheduling(current_time)
#             break
#         schedule.run_pending()
#         time.sleep(1)
