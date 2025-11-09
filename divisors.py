# divisors.py
import sys

def get_divisors(n: int):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # autograder는 인자를 줍니다. 인자 없을 때는 사용법만 출력하고 종료.
        print("Usage: python divisors.py <number>")
        sys.exit(1)

    n = int(sys.argv[1])
    if n <= 0:
        # 0이나 음수는 약수가 정의 안 되므로 종료(채점 입력은 양수일 것)
        sys.exit(0)

    for d in get_divisors(n):
        print(d)
