# 10진수 -> 2진수로 변환 구현

tar = 149
result = []

while tar != 0:
    remain = tar % 2
    result.append(remain)

    tar //= 2

result.reverse()
print(result)