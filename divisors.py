# divisors.py
import sys

# 입력 처리 (argv 또는 stdin 둘 다 가능)
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(sys.stdin.read().strip())

# 약수 출력
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
