# divisors.py
import sys

# 1️⃣ 입력값 받기 (명령행 인자 우선)
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    data = sys.stdin.read().strip()
    if not data:
        sys.exit(0)
    n = int(data)

# 2️⃣ 약수 출력
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
