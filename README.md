# B2B SaaS Event Data Scraper

This Python script is designed to scrape information about various B2B SaaS events from their respective websites. It collects data such as event dates, locations, descriptions, key speakers, and more. The scraped data is then saved in JSON format.

## Features

- Scrapes data from multiple B2B SaaS event websites
- Extracts key information such as event name, dates, location, description, speakers, etc.
- Handles different website structures with custom scraping functions
- Saves the collected data in JSON format


## Installation
    pip install -r requirements

## Usage
1. Run the script:
```
  python main.py
```
2. The script will scrape data from the following events:
- SaaStr Annual 2024
- INBOUND 2024
- B2B Marketing Exchange 2024
- SaaStock Europe 2024
- B2BRocks 2024

3. After successful execution, the json file will be generated in the same directory:
- `event_data.json`: Contains the scraped data in JSON format.

## Functions

- `get_saastr_annual_data()`: Scrapes data from the SaaStr Annual website.
- `get_inbound_data()`: Scrapes data from the INBOUND website.
- `get_b2b_marketing_exchange_data()`: Scrapes data from the B2B Marketing Exchange website.
- `get_saastock_europe_data()`: Scrapes data from the SaaStock Europe website.
- `get_b2b_rocks_data()`: Scrapes data from the B2BRocks website.
- `get_event_data(url)`: Determines which scraping function to use based on the provided URL.

## Data Structure

The scraped data for each event includes:

- Event Name
- Event Date(s)
- Location
- Website URL
- Description
- Key Speakers
- Agenda/Schedule
- Registration Details
- Pricing
- Categories
- Audience Type

## Error Handling

If the script fails to scrape data from a particular event, it will print an error message with the event name and the corresponding error. This allows for easy debugging and ensures that the script continues to run even if one event fails.

## Limitations

- The script relies on the current structure of the event websites. If the websites undergo significant changes, the scraping functions may need to be updated.
- Some information might be missing or marked as "N/A" if it's not available on the website or if the scraping fails for that particular field.
