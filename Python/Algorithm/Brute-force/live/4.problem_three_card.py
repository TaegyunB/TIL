# 카드 5장을 뽑아라
# 5장 뽑았을 때, 연속된 3개가 나오면 counting

card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(cnt):
    global result

    if cnt == 5:
        # 연속된 3개가 나오면 counting
        if count_three():
            result += 1
            print(path)
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()

recur(0)