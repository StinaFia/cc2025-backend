from flask import Flask, request

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
    print(input_data)

    # sentimen analysis
    # pickle
    return {"input_data": input_data, "message": "Hello!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)