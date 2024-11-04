# training_tracker

This application processes natural language input to record workout data, including the workout name and duration in minutes. It retrieves data from the Nutritionix API, calculates the calories burned, and logs the information into Google Sheets using the Sheety API.

## Features

- Accepts natural language input for workout names and durations.
- Retrieves workout details and calorie information from the Nutritionix API.
- Logs workout data, including date and time, into Google Sheets using Sheety API.

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required libraries:

   ```bash
   pip install requests python-dotenv
