# Import necessary libraries
from pip._vendor import requests #Library for making HTTP requests
from pprint import pprint as pp # Pretty-print library for formatting output

# Define a function to retrieve country data from the REST Countries API by name
def get_country_data_by_name(country_name):
    
    # Make an HTTP request to the API
        api_response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')

    # Check if the request was successful
        if api_response.status_code == 200:
            # Get the country data from the response
            rest_api = api_response.json()
            
            with open('vacation_spot.txt','w') as text_file:
            #with open('vacation_spot.txt', 'w', encoding='utf-8') as text_file: #This is used when having a unicode error for a country.

            # Extract the required parameters and return them as a dictionary
                # --- Construct a formatted message using f-strings for readability ---
                message = "{name} is considered as a good location for vacation. It has a population of {population} with the {timezones}timezone(s).\nThe capital of {name} is {capital}. It is located under the {continents} continent. \nThe major language(s) spoken is/are {languages}. The region in {name} is {region} while the subregion is {subregion}.\nAs a result of its state of independence being {independence}, it is {status} as a country for vacation.\nThe currency used in {name} is {currencies}.\n\n".format(
                    name = rest_api[0]['name']['official'],
                    timezones = ", ".join(rest_api[0]['timezones']),
                    capital = rest_api[0]['capital'][0],
                    independence = rest_api[0]['independent'],
                    status = rest_api[0]['status'],
                    languages = rest_api[0]['languages'],
                    currencies = rest_api[0]['currencies'],
                    continents = rest_api[0]['continents'][0],
                    population = rest_api[0]['population'],
                    region = rest_api[0]['region'],
                    subregion = rest_api[0]['subregion']
                )
                text_file.write(message) # --- Write the formatted message to the text file ---
                print("The data for your desired country has been written to 'vacation_spot.txt' file.")
             # --- Handle unsuccessful requests by printing an error message ---
        else:
            print(f"Failed to fetch country data. Status code: {api_response.status_code}")


print("\tWelcome to Rest Travels/Age Insight App!!!\n\tLet's help you get information about your desired vacation spot.\n\tYou can also see your predicted age when you input your name.")
# Example usage:
        # --- Prompt the user to enter a country name ---
country_name = input('Please enter the name of your desired country for vacation: ') # Get input from the user
# --- Retrieve country data from the API ---
data = get_country_data_by_name(country_name) # Call the function to fetch data


# Function to predict ages and save results to a text file
def predict_age(user_prompt, name_to_predict):
    """Predicts ages for a list of names using the Agify API and writes results to a text file.

   Argument:
       name_to_predict (input): Get response from the user.
   """
    
    with open('vacation_spot.txt','a') as text_file: # Append this text file to the previous text file
            agifyurl = f'https://api.agify.io/?name={name_to_predict}' # Construct API URL with name
            agify_response = requests.get(url=agifyurl) # Send GET request to API
 
            if agify_response.status_code == 200: # Check for successful response
                agify = agify_response.json() # Parse JSON response

 # Extract relevant data and format message
                message = "\tAt {count} count, the API predicted {name}'s age as: {age}\n".format(
                    count = agify['count'], # Number of people in the dataset with the given name
                    name = agify['name'], # The name for which the prediction was made
                    age = agify['age'] # The predicted age
                )      
                text_file.write(message) # Write formatted message to text file
            else:
                print(f"Error: {agify_response.status_code}, {agify_response.name}") # Print error message

#Ask the user if they would like to see the predicted ages of group members.
user_prompt = input("Would you like to see your age being predicted (yes/no)? ")
if user_prompt == 'yes': 
    print("\tNow, let's see your predicted age.")
    # List of names to predict ages for
    name_to_predict = input("Enter your name to see your predicted age: ")
    predict_age(user_prompt, name_to_predict)
    print("Your predicted age has been added to 'vacation_spot.txt' file.")
elif user_prompt == 'no':
    print("Thank you for your input!")
# Call the function to predict ages and save results
