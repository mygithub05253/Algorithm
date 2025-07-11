n = int(input())
count = 0
num = 666

# 숫자를 문자열로 변환해서 "666" 포함 여부 확인
while True:
    # 문자열에 "666"이 포함되어 있는 지 확인
    if '666' in str(num):
        count += 1
        # n번째 종말의 수에 도달했는 지 확인
        if count == n:
            print(num)
            break
    # 숫자를 하나씩 증가시키면서 브루트포스 방식으로 탐색
    num += 1