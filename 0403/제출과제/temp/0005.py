integer = int(input("정수를 입력하시오: "))

#if integer % 6
if not (integer % 2 or integer % 3):
    print("2와 3으로 나누어 떨어집니다")
else:
    print("2와 3으로 나누어 떨어지지 않습니다")
