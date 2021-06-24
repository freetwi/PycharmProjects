base = 7
x = int(input())
while x > 0:
    digit = x % base  # взять последную цифру
    print(digit, end='')
    x //= base  # зачеркнуть последую цифру
