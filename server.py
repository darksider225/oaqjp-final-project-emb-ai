''' Executing this function initiates the application of emotion
    prediction to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetector.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyse = request.args.get("textToAnalyze")
    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyse)
    # Extract the label and score from the response
    label = response['label']
    score = response['score']
    # Check if label is None
    if label is None:
        return "Invalid input! Try again"
    # Return a formatted string with the sentiment label and score
    return f"The text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host = "0.0.0.0", port = 5000)
