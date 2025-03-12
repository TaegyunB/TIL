def f(i, N):  # p[i]를 결정하는 함수
    if i == N:  # 결정이 끝나면
        print(p)

    else:
        for j in range(N):  # used에서 사용하지 않은 숫자 확인
            if used[j] == 0:  # p에 a[j]가 들어있지 않으면
                used[j] = 1
                p[i] = a[j]
                f(i+1, N)
                used[j] = 0


a = [1, 2, 3, 4, 5]
N = len(a)
p = [0] * N
used = [0] * N
f(0, N)