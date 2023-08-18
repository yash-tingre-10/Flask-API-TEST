from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_greeting():
    language = request.args.get('lang')
    greetings = {
        'English': 'Hello',
        'French': 'Bonjour le monde!',
        'Hindi': 'Namastey sansar!',
        'Default': 'Hello!'
    }

    greeting = greetings.get(language, greetings['Default'])
    return jsonify(message=greeting)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
