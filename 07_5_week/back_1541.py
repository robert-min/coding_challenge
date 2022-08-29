# 양수, +, -, => ()를 넣어서 
# return 식의 값 최소
# 두 개 이상 연산자X, 5자리보다 많이 연속되는 수X
# 55-50+40 => - 기준으로 나머지 괄호 안에 수로
# eval()

ori_ex = input()

new_ex = ""
temp = 0
check = 1
for i in ori_ex:
    # 예외 처리
    if i == "0" and check:
        pass
    else:
        new_ex += i
        if i == "-" or i == "+":
            check = 1
        else:
            check = 0

        if i == "-" and not temp:
            new_ex += "("
            temp = 1
        elif i == "-" and temp:
            new_ex += ")"
            temp = 0


if temp:
    new_ex += ")"

print(eval(new_ex))
    
