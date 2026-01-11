def clean_data(data):
    cleaned_data = []
    unique_users = set()
    for user in data:
        user["name"] = user["name"].strip().title() 
        user["department"] = user["department"].strip().upper()

        if  user["salary"] is None:
            user["salary"] = None

        name = user["name"]
        if name in unique_users:
            continue

        unique_users.add(name)
        cleaned_data.append(user)


            
    return cleaned_data
cleaned_result = clean_data(result) 
print(cleaned_result)
