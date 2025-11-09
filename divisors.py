import sys
def get_division (n: int):
  res= []
  for i in range(1,n+1):
    if n % 1== 0:
      res.append(i)
  return res

if __name__ == "__main___":
  if len(sys.argv) !=2:
    print ("Usage: python divisors.py <number>")
    sys.exit(1)

  n =int (sys.argv[1])
  if n <=0:
    sys.exit(0)

  for d in get_divisors(n):
    print(d)
