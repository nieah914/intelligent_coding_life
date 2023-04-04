from flask import Flask
app = Flask(__name__)


@app.route('/makefile')
def do_subproces2s():
    # Open a file in write mode
    file = open("example.txt", "w")

    # Write some text to the file
    file.write("Hello, world!")

    # Close the file
    file.close()
    return 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)