import requests
import json

# Base URL for data source
BASE_URL = "https://bgknowhow.com/bgjson/output"

# Entities to fetch and their corresponding file names, including postfixes
ENTITIES = {
    "bg_minions_active": "minions_active.json",
    "bg_heroes_active": "heroes_active.json",
    "bg_quests_active": "quests_active.json",
    "bg_rewards_active": "rewards_active.json",
    "bg_spells_active": "spells_active.json",
    "bg_buddies_all": "buddies_all.json",
}

def fetch_data(filename):
    """
    Fetch data for a given entity from the external API.
    """
    url = f"{BASE_URL}/{filename}"  # Construct the full URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {url}: {response.status_code}")
        return None

def preprocess_data(data):
    """
    Preprocess the fetched data by removing unnecessary fields.
    """
    if "data" in data:  # Assuming the relevant data is nested under a 'data' key
        for item in data["data"]:
            # Remove specified fields
            item.pop('picture', None)
            item.pop('pictureSmall', None)
            item.pop('picturePortrait', None)
            item.pop('pictureWhole', None)
            item.pop('flavor', None)
            if 'websites' in item:
                del item['websites']  # Remove the entire 'websites' dictionary
            # Implement additional preprocessing steps as required
    return data

def save_data(filename, data):
    """
    Save the preprocessed data to a JSON file named after the entity.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    for entity, filename in ENTITIES.items():
        print(f"Processing {entity}...")
        data = fetch_data(f"{entity}.json")
        if data is not None:
            preprocessed_data = preprocess_data(data)
            save_data(filename, preprocessed_data)
        else:
            print(f"Failed to fetch data for {entity}.")

if __name__ == "__main__":
    main()
