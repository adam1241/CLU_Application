# CLU (Conversational Language Understanding) Application

## Overview

This CLU (Conversational Language Understanding) application utilizes Azure's CLU service to analyze and understand natural language queries related to recipe cooking. It allows users to submit text queries and retrieves the intent behind those queries based on predefined tags related to recipe cooking.

## Features

- Analyzes natural language queries to determine intent related to recipe cooking.
- Supports various intents, including finding recipes, listing ingredients, dietary restrictions, and more.
- Utilizes Azure CLU service for natural language understanding.

## Prerequisites

Before using the CLU application, make sure you have the following:

- An Azure account with access to the CLU service.
- Environment variables set up for `app_id`, `subscription_key`, and `endpoint` to authenticate with the CLU service.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/adam1241/CLU_Application.git
```

2. Install the required Python packages:

```
pip install requests 
pip install pytest
```

## Usage

1. Set up environment variables for `app_id`, `subscription_key`, and `endpoint` with your Azure CLU credentials.

2. Instantiate the `LUISengine` class with your credentials

3. Use the `get_intent(query)` method to retrieve the intent for a given text query:

You can look at the file LUIS_usage.py to see how calling the engine translates to code.

## Tests

The application includes pytest tests to verify the functionality of the `get_intent` method. Run the tests using the following command:

```
pytest LUIS_tests.py
```

## Author

- Adam LAGSSAIBI


