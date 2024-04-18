# Habbit_Tracking_Project_Python

# Pixela Graph Tracker

Pixela Graph Tracker is a Python script that interacts with the Pixela API to create a user account, define a graph, and post data to the graph to track daily activities. In this example, we're tracking the time spent on coding each day.

## Components

### 1. Create Account

The script sends a POST request to the Pixela API to create a new user account. It provides the required parameters such as token, username, and agreement to terms of service.

### 2. Create Graph

Once the account is created, the script defines a graph using the user's token and username. It specifies the graph ID, name, unit (e.g., minutes), type (e.g., integer), and color.

### 3. Post Graph Data

Using the created graph, the script posts data points to the graph to track daily activities. It sends a POST request with the date and quantity of the activity for the current day.

## Dependencies

- **Requests**: HTTP library for making API requests.
- **Datetime**: Module for working with dates and times in Python.

## Setup

1. Obtain an API token from the Pixela website.
2. Install the required Python library: `requests`.
3. Replace the placeholders (`APITOKEN`, `USERNAME`) with your Pixela API token and username.
4. Run the Python script to create a user account, define a graph, and post data to the graph.

