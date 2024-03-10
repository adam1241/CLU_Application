# Install the requests library if it is not already installed.
#pip install requests 

import requests 
from dotenv import load_dotenv
import os

# Loading environment variables 
load_dotenv()

# Retrieving values of environment variables 
API_VERSION = os.getenv('API_VERSION')
PROJECT_NAME = os.getenv('PROJECT_NAME')
DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME')

class LUISengine:
    # Initialize the LUIS engine with the provided app ID, subscription key, and endpoint.
    def __init__(self, app_id, subscription_key, endpoint):
        self.app_id = app_id
        self.subscription_key = subscription_key
        self.endpoint = endpoint

    # Retrieve the confidence score for a specific category from a list of categories.
    @staticmethod
    def get_confidence_score(categories, target_category):
        for category in categories:
            if category["category"] == target_category:
                return category["confidenceScore"]
        # If the target category is not found, return None.
        return None
    
    # Get the intent of a given query using the LUIS engine.
    def get_intent(self, query):
        # Construct the URL for making the API request.
        url = f"{self.endpoint}/language/:analyze-conversations?api-version={API_VERSION}-preview"

        # Prepare the data to be sent in the request body.
        data = {
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "id": "PARTICIPANT_ID_HERE",
                    "text": query,
                    "modality":"text",
                    "language":"en",
                    "participantId":"PARTICIPANT_ID_HERE"
                }
            },
            "parameters": {
                "projectName": PROJECT_NAME,
                "verbose":True,
                "deploymentName": DEPLOYMENT_NAME,
                "stringIndexType": "TextElement_V8"
            }
        }
        
        # Define the headers for the request.
        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Apim-Request-Id":self.app_id,
            "Content-Type": "application/json"
        }

        # Make the POST request to the LUIS engine API.
        response = requests.post(url, json=data, headers=headers)
        response_dict = response.json()

        # If the request is successful (status code 200), extract the top intent and confidence score.
        if response.status_code == 200:
            topIntent = response_dict['result']['prediction']['topIntent']
            confidence_score = LUISengine.get_confidence_score(response_dict['result']['prediction']['intents'], topIntent)
            return topIntent, confidence_score
        else:
            # If the request fails, print the error message.
            print(f"the Requirement failed , state: {response.status_code}:")
            print(response.text)

