clients, tariffs = map(int, input().split())
payments = list(map(int, input().split()))  # длины clients
payments.sort()
result = []
sum = 0
for payment in payments:
    if 1 <= payment <= 10**9 and len(result) <= tariffs:
