import json
import datetime

def convert_user_id(user_id):
    # Convert user ID string to BigInt
    userIDInt = 0
    for char in user_id:
        userIDInt = userIDInt * 36 + int(char, 36)

    # Shift right by 64 bits
    userIDInt >>= 32
    userIDInt >>= 32

    # Convert to a number
    myNumber = userIDInt

    # Convert to a date
    joinDate = datetime.datetime.fromtimestamp(myNumber / 1000)

    # Get Unix timestamp in milliseconds
    unixTimeMilliseconds = int(joinDate.timestamp() * 1000)

    return unixTimeMilliseconds

def format_join_date(join_date):
    # Convert join date to a human-readable format (GMT time in milliseconds)
    formatted_join_date = datetime.datetime.utcfromtimestamp(join_date / 1000).strftime("%B %dth %Y %I:%M:%S:%f %p")
    return formatted_join_date

if __name__ == "__main__":
    # Load user IDs from all_users.json
    with open("all_users.json") as f:
        user_ids = json.load(f)

    # Convert user IDs to dates and assign sequential numbers
    users_with_dates = []
    for idx, user_id in enumerate(user_ids, start=1):
        try:
            join_date = convert_user_id(user_id)
            join_date_formatted = format_join_date(join_date)
            users_with_dates.append({"user_id": user_id, "join_date_epoch": join_date, "join_date": join_date_formatted})
        except Exception as e:
            print(f"Error converting user ID {user_id}: {e}")

    # Sort users by join date
    sorted_users = sorted(users_with_dates, key=lambda x: x["join_date_epoch"])

    # Assign sequential IDs starting from 1
    for idx, user in enumerate(sorted_users, start=1):
        user["ID"] = idx

    # Save sorted users to oldest_users.json
    with open("oldest_users.json", "w") as f:
        json.dump(sorted_users, f, indent=4)

    print("Conversion and sorting complete. Results saved to oldest_users.json.")
