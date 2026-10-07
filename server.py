"""
This module initiates a Flask application for performing sentiment analysis.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyzes the sentiment of text provided via a URL query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided for analysis.", 400

    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    # Extracted formatted string to fix the line-too-long linting error
    formatted_label = label.split('_')[1]
    return f"The given text has been identified as {formatted_label} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Renders the main index interface page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
