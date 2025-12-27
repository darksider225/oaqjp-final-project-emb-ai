''' Executing this function initiates the application of emotion
    prediction to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Flask route handler that retrieves text input from request arguments,
    analyzes emotions using the emotion_detector function, and returns
    a formatted string with emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyse = request.args.get("textToAnalyze")
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    # Check If the dominant_emotion is None
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    # Else convert the recieved response to string for output
    disp_response = (
        f"For the given statement, the system response is " 
        f"'anger': {response['anger']}, " f"'disgust': {response['disgust']}, " 
        f"'fear': {response['fear']}, " f"'joy': {response['joy']} and " 
        f"'sadness': {response['sadness']}. " 
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    # Return a formatted string for output
    return disp_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host = "0.0.0.0", port = 5000)
