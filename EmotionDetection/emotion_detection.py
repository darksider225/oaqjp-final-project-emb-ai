"""
emotion_detection.py

This module provides a function for performing emotion_detection
using IBM Watson NLP services. It sends text input to the Watson
Emotion Prediction function and returns an output.

Functions:
    emotion_detector(text_to_analyse):
        Sends the given text to the Watson Emotion Prediction API.
        Returns a dictionary containing:
        'label': The sentiment classification (e.g., SENT_POSITIVE, SENT_NEGATIVE, SENT_NEUTRAL).
        'score': The confidence score associated with the prediction.

Example:
    >>> from sentiment_analysis import sentiment_analyzer
    >>> result = sentiment_analyzer("I love working with Python")
    >>> print(result)
    {'label': 'SENT_POSITIVE', 'score': 0.95}
"""
# Import the requests and json libraries to handle HTTP requests and parsing
import json
import requests
# Define a function that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    # URL of the emotion detection service.
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout = 10)
    # Check if the reponse code is 200 for error handling
    if response.status_code == 200:
        # Parsing the json response from the API
        formatted_response = json.loads(response.text)
        # Extracting data for formatting
        data = formatted_response["emotionPredictions"][0]["emotion"]
        final_response = {
            'anger': data["anger"],
            'disgust': data["disgust"],
            'fear': data["fear"],
            'joy': data["joy"],
            'sadness': data["sadness"],
            'dominant_emotion': max(data, key = data.get)
            }
        return final_response
    # Check if the error code is 400 to identify blank entries
    elif response.status_code == 400:
        final_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
        return final_response