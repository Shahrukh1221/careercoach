from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Process the incoming JSON payload and trigger the appropriate action
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
