# divisors.py
import sys

n = int(sys.argv[1])  # 명령행 인자로 입력된 숫자 받기

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
