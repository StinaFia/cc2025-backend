import os
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    print('hello')
    return "<p>Hello, World! Version 2.1</p>"

# demonstration how to get JSON data from the user
@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json

    # access the posted data
    text = input_data["text"]

    # Load the sentiment analysis model 
    # https://colab.research.google.com/drive/1jwjmSodT7yjfwHyMZEKXnOIbl9uiDfZL#scrollTo=cwHXD4a6j5OK
    with open("sentiment_model.pkl", "rb") as f:
        text_clf = pickle.load(f)

    prediction = text_clf.predict([text])[0]

    # return prediction result as JSON
    return {"input_text": text, "prediction": str(prediction)}


#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port="8080", debug=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)