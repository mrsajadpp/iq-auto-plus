import requests
import json
import random
from faker import Faker

# Initialize Faker with Indian localization
fake = Faker('en_IN')

# API Endpoint
api_url = "https://api.manoramaquiz.in/v1/userManagement"

# Output file to store email and DOB
output_file = "user_data.json"

# Kerala-based first and last names
first_names = [
    "Abhilash", "Akhil", "Anjali", "Anju", "Arya", "Arun", "Ashwin", "Athira", "Balakrishnan", "Bhavana", 
    "Chandran", "Chitra", "Deepak", "Deepa", "Devika", "Dinesh", "Divya", "Fathima", "Ganesh", "Gautham", 
    "Gayathri", "Girish", "Hari", "Harikrishnan", "Haritha", "Indira", "Indrajith", "Jayasree", "Jeevan", 
    "Jyothi", "Kalyani", "Kiran", "Krishna", "Krishnan", "Lekha", "Lijo", "Madhavi", "Madhavan", "Manoj", 
    "Manu", "Mathew", "Meera", "Mohan", "Muralidharan", "Nandana", "Nandan", "Naveen", "Neethu", "Neha", 
    "Nikhil", "Nimisha", "Nithin", "Padma", "Parvathy", "Pradeep", "Prakash", "Pranav", "Prasanna", 
    "Prem", "Priya", "Radhika", "Rahul", "Rajeev", "Rajesh", "Rakesh", "Ramesh", "Ranjith", "Rekha", 
    "Renjith", "Reshma", "Revathi", "Rohit", "Sajeev", "Sajith", "Sanal", "Sandhya", "Saranya", "Sarath", 
    "Sathish", "Satyajith", "Seema", "Shalini", "Sharath", "Sibin", "Siddharth", "Sinu", "Sreejith", 
    "Sreekumar", "Sreekutty", "Sreekanth", "Sreeraj", "Sreenath", "Sreesanth", "Sreekala", "Subhash", 
    "Suma", "Suresh", "Sushma", "Swapna", "Syam", "Thara", "Uma", "Unnikrishnan", "Varsha", "Venu", 
    "Vidya", "Vijay", "Vineeth", "Vinod", "Vishnu", "Yamuna", "Anoop", "Athul", "Arathi", "Chandrika", 
    "Devan", "Elizbeth", "Govind", "Haridas", "Ishwar", "Jithin", "Karthik", "Lakshmi", "Malini", 
    "Niranjan", "Rajendran", "Ramya", "Santhosh", "Shaji", "Sheeba", "Sindhu", "Suraj", "Usha", 
    "Vijayan", "Aswin", "Anand", "Akash", "Faisal", "Jaseela", "Jesna", "Shine", "Mithun", "Roopa", 
    "Sherin", "Shibin", "Abhirami", "Sanju", "Anitta", "Neeraj", "Sona", "Gokul", "Darshan", "Alok", 
    "Anikha", "Nanditha", "Lakshman", "Arathi", "Siddique", "Kavya", "Ajay", "Ambili", "Kavitha", 
    "Surya", "Ravi", "Ajith", "Maya", "Anagha", "Adarsh", "Chippy", "Devu", "Daya", "Sethu", 
    "Narayanan", "Midhun", "Aiswarya", "Praveen", "Padmakumar", "Teena", "Archa", "Anandhu", 
    "Keerthi", "Jithesh", "Sruthy", "Vimal", "Leela", "Femi", "Anjana", "Vipin", "Kamal", "Jayakrishnan"
]

last_names = [
    "Achuthan", "Achari", "Antony", "Appukuttan", "Balakrishnan", "Balan", "Chacko", "Chandran", "Cheeran", 
    "Cherian", "Damodaran", "Das", "Devassy", "Devan", "Eapen", "Edathil", "Ganapathy", "Gopakumar", 
    "Govindan", "Hariharan", "Iyer", "Jacob", "Jayakumar", "John", "Joseph", "Joy", "Kamalasanan", 
    "Karunakaran", "Kartha", "Keshavan", "Krishnan", "Kurian", "Kuttan", "Madhavan", "Mathew", "Menon", 
    "Moideen", "Mohan", "Mukundan", "Nambiar", "Narayanan", "Nayar", "Ninan", "Padmanabhan", 
    "Panicker", "Pillai", "Ponnappa", "Prabhakaran", "Raghavan", "Rajagopal", "Raman", "Ravindran", 
    "Sankaran", "Sasikumar", "Sethumadhavan", "Shenoy", "Sreekumar", "Subramanian", "Sudhakaran", 
    "Sukumaran", "Sundaresan", "Tharakan", "Thomas", "Unnikrishnan", "Varghese", "Varma", "Vijayan", 
    "Warrier", "Achary", "Aiyer", "Chittilappilly", "Dhanapalan", "Edachery", "Govindarajan", "Ishwaran", 
    "Jayadevan", "Kizhakkedath", "Kollam", "Mangalassery", "Mangalathu", "Marar", "Mathewkutty", 
    "Mathukutty", "Meledath", "Moorthi", "Nair", "Nampoothiri", "Narayanan", "Pallipparambil", 
    "Parameswaran", "Pattathil", "Pulickal", "Radhakrishnan", "Raja", "Rajesh", "Ramachandran", 
    "Sadasivan", "Sasidharan", "Shankar", "Shanavas", "Shekhar", "Shivaram", "Somasekharan", "Sundar", 
    "Thangal", "Tharavadu", "Thekkedath", "Vadakkan", "Vadassery", "Vaidyanathan", "Vasudevan", 
    "Velappan", "Velayudhan", "Venkatesh", "Vettathu", "Vishwanathan", "Yatheendra", "Abraham", 
    "Chennithala", "Cheruvathur", "Cherukara", "Devanandan", "Devendran", "Gopalakrishnan", 
    "Jayaram", "Kesavan", "Kumaran", "Narasimhan", "Padmanaban", "Parvathi", "Prathapan", 
    "Ramalingam", "Rangaswamy", "Rasool", "Subrahmanian", "Sulochana", "Thankappan", "Tirunelveli"
]

roles = [
    {"roleId": "670e850968ede49b0fae399a", "roleName": "Parents"},
    {"roleId": "670e850968ede49b0fae399b", "roleName": "Alumni"}
]

# Custom function to generate Kerala-based names
def generate_kerala_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name, last_name

# Function to generate fake user data with Kerala-based names
def generate_fake_user():
    first_name, last_name = generate_kerala_name()
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
        "roleObj": random.choice(roles)
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
    total_users = 999
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
