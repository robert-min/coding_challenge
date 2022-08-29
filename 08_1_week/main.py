from collections import defaultdict

def solution(clothes):
    answer = 0
    t = 1
    # 의상들이 담긴 2차원배열 -> list, [이름, 종류]
    # return : 서로 다른 옷의 조합의 수
    
    # default 딕셔너리로 정리
    temp = defaultdict(list)
    for cloth in clothes:
        temp[cloth[1]].append(cloth[0])
    
    for c in temp.values():
        answer += len(c)
        t *= len(c)
    answer += t
    
    # 하나만 입었을 때 : 각 개수
    # 서로 다른 조합 입었을 때 : 각 개수 * 각 개수
    
    return answer

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))