# Overview of Agify and Rest Countries API
Agify API was used to predict the ages of Group 1 members while Rest Countries was used to suggest Vacation spots in different countries.


# Agify Age Prediction
This Python script uses the Agify API to predict the ages for a list of names and saves the results to a text file. Follow the steps below to run the code.
 
1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **Requests Library:** Install the `requests` library, which is used for making HTTP requests.
3. Clone or download this repository to your local machine.
4.  Open a terminal and navigate to the directory containing the script.
5. Run the script using the following command: python Rest_Age.py
6. The script will make requests to the Agify API for each name in the list and print the results to the terminal. The results will be saved to a text file named 'group_members_age_prediction.txt.'
7. If you want to predict ages for a different set of names, modify the 'name_to_predict' list in the script. Add or remove names based on your preferences.
 
 
# Rest Countries
 
This Python script retrieves information about a country using the REST Countries API and suggests it as a potential vacation spot. The retrieved data includes details like population, timezones, capital, languages spoken, and more.
 
## Prerequisites
 
1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **Requests Library:** Install the `requests` library, which is used for making HTTP requests. Run the following command in your terminal:
 
   ```bash
   pip install requests
 
3. Clone or download this repository to your local machine.
4. Open a terminal and navigate to the directory containing the script.
5. The script will prompt you to enter the name of the country you are interested in. Type the name and press Enter.
6. The script will make a request to the REST Countries API, fetch data about the specified country, and print the details on the terminal.
7. **Customizing the Country:** If you want information about a different country, simply run the script again and enter the name of the desired country when prompted.
 
 
# Collaborators and assigned tasks
 
1. Fatima - Import status and calling out the response
2. Kate and Busayo - Writing it to text file; Agify
3. Blessing - Added user- input to the rest_api function
4. Omobolanle - Defined the rest function
5. Janetoms - Writing it to text file; Rest countries
6. Jesulolufemi - Added comments to both APIs
