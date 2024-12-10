import requests
import json
from faker import Faker
import random

# Initialize Faker with Indian localization
fake = Faker('en_IN')

# API Endpoint
api_url = "https://api.manoramaquiz.in/v1/userManagement"

# Output file to store email and DOB
output_file = "user_data.json"

# Function to generate fake user data with custom email format
def generate_fake_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_code = random.randint(1000, 9999)
    email = f"{first_name.lower()}{last_name.lower()}{random_code}@gmail.com"
    phone = fake.phone_number()
    dob = fake.date_of_birth(minimum_age=10, maximum_age=20).strftime("%Y-%m-%d")
    
    user_data = {
        "name": f"{first_name} {last_name}",
        "schoolId": "672c44e27d4653e446a78b5c",  # Static value, replace if dynamic
        "phone": phone,
        "email": email,
        "dob": dob,
        "roleObj": {
            "roleId": "670e850968ede49b0fae3998",  # Static value, replace if dynamic
            "roleName": "Students"
        }
    }
    return user_data

# Function to call the API and handle response
def signup_user(user_data):
    try:
        response = requests.post(api_url, json=user_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Main function
def main():
    total_users = 400
    users_list = []  # List to store user email and DOB
    
    for count in range(1, total_users + 1):
        user_data = generate_fake_user()
        
        response_data = signup_user(user_data)
        if response_data and response_data.get('statusCode') == 201:
            print(f"Successfully signed up user {count}: {user_data['email']}")
            # Add email and DOB to users list
            users_list.append({"email": user_data["email"], "dob": user_data["dob"]})
        else:
            print(f"Failed to sign up user {count}")
        
        # Print progress at every 10th user
        if count % 10 == 0:
            print(f"Signup progress: {count}/{total_users} users completed.")
    
    # Save all user data to JSON file as an array
    try:
        with open(output_file, "w") as f:
            json.dump(users_list, f, indent=4)
        print(f"All user data saved to {output_file}")
    except IOError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main()
