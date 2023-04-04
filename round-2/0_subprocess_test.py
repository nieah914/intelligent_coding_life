import subprocess

# 텍스트를 입력 받는다.
data = input()

proc = subprocess.Popen(data
		, shell=True
		, stdout=subprocess.PIPE
		, stderr=subprocess.PIPE
		, stdin=subprocess.PIPE) # subprocess의 입출력 설정

stdout_value = proc.stdout.read() + proc.stderr.read() # 실행 결과에 대한 내역 저장
print(stdout_value.decode(encoding='CP949')) # 바이너리 실행 결과를 알아볼수 있도록 출력