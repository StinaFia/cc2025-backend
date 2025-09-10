from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print('hello')
    return "<p>Hello, World! Version 1.1</p>"

# demonstration how to get JSON data from the user
@app.route('/data', methods=['POST'])
def get_data():
    data = request.json
    # access the posted data
    print(data["name"])
    return {"message": "Data received", "data": data}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)