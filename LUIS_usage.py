from LUIS import LUISengine 
from dotenv import load_dotenv
import os

# Loading environment variables 
load_dotenv()

# Retrieving values of environment variables 
app_id = os.getenv('app_id')
subscription_key = os.getenv('subscription_key')
endpoint = os.getenv('endpoint')


def main():
    # Creating an instance of the LUISengine class with provided parameters
    clu_client = LUISengine(app_id, subscription_key, endpoint)
    
    # Defining a query to be sent to the LUIS engine
    query = "Find a recipe for pasta"
    
    # Calling the get_intent method of the clu_client instance and storing the returned intent and confidence score
    intent, confidence_score = clu_client.get_intent(query)
    
    # Printing the obtained intent and confidence score
    print("Intent:", intent, "confidence_score:", confidence_score)

# Calling the main function to execute the program
main()
