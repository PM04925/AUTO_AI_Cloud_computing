import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)


API_KEY = "<API key>"
# check PPT for API


token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
print(token_response.json())
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
array_of_input_fields = ["COLUMN1",	"Name",	"Age",	"Marital Status",	"Education Level",	"Number of Children",	"Smoking Status",	"Physical Activity Level",	"Employment Status",	"Income",	"Alcohol Consumption",	"Dietary Habits",	"Sleep Patterns",	"History of Mental Illness",	"History of Substance Abuse",	"Family History of Depression",	"Chronic Medical Conditions"]

array_of_values_to_be_scored = [0,	"Christine Barker",	31	,"Married",	"Bachelor's Degree",	2,	"Non-smoker",	"Active",	"Unemployed",	26265.67,	"Moderate",	"Moderate",	"Fair",	"Yes",	"No",	"Yes",	"Yes"]

payload_scoring = {"input_data": [{"fields": array_of_input_fields, "values": array_of_values_to_be_scored}]}

response_scoring = requests.post('https://private.us-south.ml.cloud.ibm.com/ml/v4/deployments/19854149-8930-42ad-a34f-ae369a342d1b/predictions?version=2021-05-01', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())