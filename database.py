# import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = "d0sas5umwhg_9N2kpDnHvw2jiWRg3XfddCniXjNCoan4"
# st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("survey")


def insert_period(projectName,demodate,location,attendeeName,attendeetype,demoType,expectation,likes,dislikes,satisfaction,recommendation):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"projectName": projectName, "demodate": demodate, "location": location, "attendeeName": attendeeName, "attendeetype": attendeetype, "demoType": demoType, "expectation": expectation, "likes": likes, "dislikes": dislikes,"satisfaction":satisfaction,"recommendation":recommendation})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

