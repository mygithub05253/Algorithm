n = int(input())
min_bags = -1  # 기본값은 -1 (불가능한 경우)

# 5kg 봉지를 가능한 최대한 많이 쓰는 경우부터 줄여가면서 탐색하는 방식
for five_kg in range(n // 5, -1, -1):
    remaining = n - (five_kg * 5)
    
    # 남은 무게가 3kg으로 나누어 떨어지는 경우에만 유효한 조합
    if remaining % 3 == 0:
        three_kg = remaining // 3
        
        # 현재 조합에서 사용한 봉지 수의 총합 구하기
        min_bags = five_kg + three_kg
        
        # 가장 먼저 찾은 유효한 조합이 최소 봉지 수이기 때문에 바로 종료
        break
print(min_bags)