import json

# Step 1: Load data
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

result = load_data("store_data.json")
print(result)
def clean_data(data):
    rating_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    cleaned_data = []
    unique_users = set()

    for user in data:
        # clean rating
        raw_rating = user["rating"]
        if isinstance(raw_rating, str):
            raw_rating = raw_rating.strip().lower()
            if raw_rating in rating_map:
                raw_rating = rating_map[raw_rating]
        user["rating"] = raw_rating

        # fill missing age
        if user.get("age") is None:
            user["age"] = None

        # deduplication by name
        name = user["name"].strip()
        if name in unique_users:
            continue

        unique_users.add(name)
        cleaned_data.append(user)

    return cleaned_data
cleaned_result = clean_data(result)
print(cleaned_result)
def get_insights(cleaned_data):
    total_rating = 0
    count = 0
    user_count = 0

    for user in cleaned_data:
       


        total_rating += float(user["rating"])
        count += 1

        if float(user["rating"]) < 3:
            user_count += 1

    if count == 0:
        print("No valid ratings found")
        return

    avg_rating = total_rating / count
    bad_rating_user = (user_count / count) * 100

    print(f"Average user rating: {avg_rating}")
    print(f"Percentage of users giving rating below 3: {bad_rating_user}%")
get_insights(cleaned_result)
def recommendations(data):
    recommen = []
    curr_recom = {}
    for user in data:
        curr_recom = {}
        curr_recom["name"] = user["name"]
        if float(user["rating"])>=4:
            curr_recom["brand"] = "Apple"
        else:
             curr_recom["brand"] = "Samsung"
        recommen.append(curr_recom)
    return recommen
recom = recommendations(cleaned_result)
print(recom)
