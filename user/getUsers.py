import json
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

def load_data_from_splits():
    data = []
    for filename in os.listdir("."):
        if filename.startswith("split_data_") and filename.endswith(".json"):
            with open(filename) as f:
                data.extend(json.load(f))
                logging.info(f"Data loaded from {filename}")
    return data

# Load data from all split files
data = load_data_from_splits()

# Extract unique user IDs
users = []
for level in data:
    user_id = level["identifier"].split(":")[0]
    if user_id not in users:
        users.append(user_id)
        logging.info(f"User ID {user_id} added")

# Write the unique user IDs to a new file
with open("all_users.json", "w") as f:
    json.dump(users, f)
    logging.info("Unique user IDs written to all_users.json")
