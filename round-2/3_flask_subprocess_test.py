import subprocess
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        textfield = request.form['textfield']


        proc = subprocess.Popen(str(textfield)
                                , shell=True
                                , stdout=subprocess.PIPE
                                , stderr=subprocess.PIPE
                                , stdin=subprocess.PIPE)  # subprocess의 입출력 설정

        stdout_value = proc.stdout.read() + proc.stderr.read()  # 실행 결과에 대한 내역 저장
        print(stdout_value.decode(encoding='CP949'))  # 바이너리 실행 결과를 알아볼수 있도록 출력
    return render_template('index.html')


@app.route('/subprocess')
def do_subprocess():
    data = 'ls'
    proc = subprocess.Popen(data
                            , shell=True
                            , stdout=subprocess.PIPE
                            , stderr=subprocess.PIPE
                            , stdin=subprocess.PIPE)  # subprocess의 입출력 설정

    stdout_value = proc.stdout.read() + proc.stderr.read()  # 실행 결과에 대한 내역 저장
    print(stdout_value.decode(encoding='CP949'))  # 바이너리 실행 결과를 알아볼수 있도록 출력


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)