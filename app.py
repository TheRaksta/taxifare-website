import streamlit as st
from datetime import datetime
import requests

# '''
# # TaxiFareModel front
# '''

# st.markdown('''

# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time

# - import datetime
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count

# '''

st.title("Estimate the cost of a Taxi-Ride")

st.markdown("<br>", unsafe_allow_html=True)

date = st.date_input("Select a date", value=datetime.now().date())

# Time input widget
time = st.time_input("Select a time", value=datetime.now().time())

selected_datetime = datetime.combine(date, time)

# Combine the date and time
if st.button("Submit"):
    # Combine date and time into a datetime object
    selected_datetime = datetime.combine(date, time)

    # Display the selected date and time
    st.write(f"Selected Date and Time: {selected_datetime}")

st.markdown("<br>", unsafe_allow_html=True)

number1 = st.number_input('Enter the pick-up longitude')

st.markdown("<br>", unsafe_allow_html=True)

st.write('The pick-up longitude ', number1)

st.markdown("<br>", unsafe_allow_html=True)

number2 = st.number_input('Enter the pick-up latitude')

st.write('The pick-up latitude is ', number2)

st.markdown("<br>", unsafe_allow_html=True)

number3 = st.number_input('Enter the drop-off longitude')

st.write('The drop-off longitude is ', number3)

st.markdown("<br>", unsafe_allow_html=True)

number4 = st.number_input('Enter the drop-off latitude')

st.write('The drop-off latitude is  ', number4)

st.markdown("<br>", unsafe_allow_html=True)

count = st.slider('Select the number of passengers', 1, 8, 1)




# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
#

url = 'https://taxifare-633559710162.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...


# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

params = {
        'pickup_datetime': selected_datetime,
        'pickup_longitude': number1,
        'pickup_latitude': number2,
        'dropoff_longitude':number3,
        'dropoff_latitude':number4,
        'passenger_count':count
}

st.markdown("<br>", unsafe_allow_html=True)

if st.button('Click to estimate cost'):
    # print is visible in the server output, not in the page
    url = 'https://taxifare-633559710162.europe-west1.run.app/predict'

    response = requests.get(url, params)
    output = response.json()["fare"]
    # st.markdown(output)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<span style="font-size: 40px; color:blue;">**{output}**</span>', unsafe_allow_html=True)
else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write('I was not clicked 😞')
