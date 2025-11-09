# divisors.py
import sys

# 입력값 받기
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    data = sys.stdin.read().strip()
    if not data:
        sys.exit(0)
    n = int(data)

# 약수 리스트 만들기
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(str(i))

# 한 줄에 공백으로 출력
print(" ".join(divisors))
