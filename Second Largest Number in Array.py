"""arr = list(map(int, input().split())) 
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(second)


num = int(input()) 
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)
