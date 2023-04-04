from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello/<name>')
def hello(name):
    """
    A simple hello world API
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name to say hello to
    responses:
      200:
        description: A simple message
    """
    message = f'Hello, {name}!'
    return {'message': message}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8012)
