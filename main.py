import requests
from bs4 import BeautifulSoup
import json

def get_saastr_annual_data():
    url = "https://www.saastrannual2024.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    event_data = {
        "Event Name": soup.title.string.strip() if soup.title else "N/A",
        "Event Date(s)": "September 10-12, 2024",  
        "Location": "San Francisco, CA, USA",  
        "Website URL": url,
        "Description": soup.find("meta", {"name": "description"}).get("content").strip() if soup.find("meta", {"name": "description"}) else "N/A",
        "Key Speakers": [speaker.text.strip() for speaker in soup.select(".speaker-name")] if soup.select(".speaker-name") else "N/A",
        "Agenda/Schedule": [session.text.strip() for session in soup.select(".agenda-session")] if soup.select(".agenda-session") else "N/A",
        "Registration Details": soup.select_one(".registration-info").text.strip() if soup.select_one(".registration-info") else "N/A",
        "Pricing": soup.select_one(".pricing-info").text.strip() if soup.select_one(".pricing-info") else "N/A",
        "Categories": [category.text.strip() for category in soup.select(".event-category")] if soup.select(".event-category") else "N/A",
        "Audience type": soup.select_one(".audience-type").text.strip() if soup.select_one(".audience-type") else "N/A",
    }
    
    return event_data

def get_inbound_data():
    url = "https://www.inbound.com/2024"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    event_data = {
        "Event Name": soup.title.string.strip() if soup.title else "INBOUND 2024",
        "Event Date(s)": "September 18-20, 2024",  
        "Location": "Boston, MA, USA",  
        "Website URL": url,
        "Description": soup.find("meta", {"name": "description"}).get("content").strip() if soup.find("meta", {"name": "description"}) else "N/A",
        "Key Speakers": [speaker.text.strip() for speaker in soup.select(".speaker-name")] if soup.select(".speaker-name") else "N/A",
        "Agenda/Schedule": [session.text.strip() for session in soup.select(".agenda-session")] if soup.select(".agenda-session") else "N/A",
        "Registration Details": soup.select_one(".registration-info").text.strip() if soup.select_one(".registration-info") else "N/A",
        "Pricing": soup.select_one(".pricing-info").text.strip() if soup.select_one(".pricing-info") else "N/A",
        "Categories": [category.text.strip() for category in soup.select(".event-category")] if soup.select(".event-category") else "N/A",
        "Audience type": soup.select_one(".audience-type").text.strip() if soup.select_one(".audience-type") else "N/A",
    }
    
    return event_data

def get_b2b_marketing_exchange_data():
    url = "https://b2bmarketing.exchange"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    event_data = {
        "Event Name": soup.title.string.strip() if soup.title else "B2B Marketing Exchange 2024",
        "Event Date(s)": "October 1-3, 2024",  
        "Location": "Scottsdale, AZ, USA",  
        "Website URL": url,
        "Description": soup.find("meta", {"name": "description"}).get("content").strip() if soup.find("meta", {"name": "description"}) else "N/A",
        "Key Speakers": [speaker.text.strip() for speaker in soup.select(".speaker-name")] if soup.select(".speaker-name") else "N/A",
        "Agenda/Schedule": [session.text.strip() for session in soup.select(".agenda-session")] if soup.select(".agenda-session") else "N/A",
        "Registration Details": soup.select_one(".registration-info").text.strip() if soup.select_one(".registration-info") else "N/A",
        "Pricing": soup.select_one(".pricing-info").text.strip() if soup.select_one(".pricing-info") else "N/A",
        "Categories": [category.text.strip() for category in soup.select(".event-category")] if soup.select(".event-category") else "N/A",
        "Audience type": soup.select_one(".audience-type").text.strip() if soup.select_one(".audience-type") else "N/A",
    }
    
    return event_data

def get_saastock_europe_data():
    url = "https://www.saastock.com/europe/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    event_data = {
        "Event Name": soup.title.string.strip() if soup.title else "SaaStock Europe 2024",
        "Event Date(s)": "October 23-25, 2024",  
        "Location": "Dublin, Ireland",  
        "Website URL": url,
        "Description": soup.find("meta", {"name": "description"}).get("content").strip() if soup.find("meta", {"name": "description"}) else "N/A",
        "Key Speakers": [speaker.text.strip() for speaker in soup.select(".speaker-name")] if soup.select(".speaker-name") else "N/A",
        "Agenda/Schedule": [session.text.strip() for session in soup.select(".agenda-session")] if soup.select(".agenda-session") else "N/A",
        "Registration Details": soup.select_one(".registration-info").text.strip() if soup.select_one(".registration-info") else "N/A",
        "Pricing": soup.select_one(".pricing-info").text.strip() if soup.select_one(".pricing-info") else "N/A",
        "Categories": [category.text.strip() for category in soup.select(".event-category")] if soup.select(".event-category") else "N/A",
        "Audience type": soup.select_one(".audience-type").text.strip() if soup.select_one(".audience-type") else "N/A",
    }
    
    return event_data

def get_b2b_rocks_data():
    url = "https://www.b2brocks.co"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    event_data = {
        "Event Name": soup.title.string.strip() if soup.title else "B2B Rocks 2024",
        "Event Date(s)": "November 6-7, 2024",  
        "Location": "Paris, France",  
        "Website URL": url,
        "Description": soup.find("meta", {"name": "description"}).get("content").strip() if soup.find("meta", {"name": "description"}) else "N/A",
        "Key Speakers": [speaker.text.strip() for speaker in soup.select(".speaker-name")] if soup.select(".speaker-name") else "N/A",
        "Agenda/Schedule": [session.text.strip() for session in soup.select(".agenda-session")] if soup.select(".agenda-session") else "N/A",
        "Registration Details": soup.select_one(".registration-info").text.strip() if soup.select_one(".registration-info") else "N/A",
        "Pricing": soup.select_one(".pricing-info").text.strip() if soup.select_one(".pricing-info") else "N/A",
        "Categories": [category.text.strip() for category in soup.select(".event-category")] if soup.select(".event-category") else "N/A",
        "Audience type": soup.select_one(".audience-type").text.strip() if soup.select_one(".audience-type") else "N/A",
    }
    
    return event_data

def get_event_data(url):
    if "saastrannual2024" in url:
        return get_saastr_annual_data()
    elif "inbound.com" in url:
        return get_inbound_data()
    elif "b2bmarketing.exchange" in url:
        return get_b2b_marketing_exchange_data()
    elif "saastock.com" in url:
        return get_saastock_europe_data()
    elif "b2brocks.co" in url:
        return get_b2b_rocks_data()
    else:
        return {}

events = [
    {"name": "SaaStr Annual 2024", "url": "https://www.saastrannual2024.com"},
    {"name": "INBOUND 2024", "url": "https://www.inbound.com/2024"},
    {"name": "B2B Marketing Exchange 2024", "url": "https://b2bmarketing.exchange"},
    {"name": "SaaStock Europe 2024", "url": "https://www.saastock.com/europe/"},
    {"name": "B2BRocks 2024", "url": "https://www.b2brocks.co"}
]

all_event_data = []

for event in events:
    try:
        event_data = get_event_data(event["url"])
        all_event_data.append(event_data)
    except Exception as e:
        print(f"Failed to scrape {event['name']} at {event['url']}: {e}")


with open('event_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_event_data, f, indent=4, ensure_ascii=False)

print("Scraping completed. Data saved to 'event_data.json'")