def main():
    # 1. 숫자 입력 받기
    try:
        num_str = input("Enter number: ")
        # 입력받은 문자열을 소수점까지 포함하는 숫자(float)로 변환
        number = float(num_str)
    except ValueError:
        # 숫자로 변환할 수 없을 경우 예외 처리
        print("Invalid number input.")
        return # 프로그램 종료

    # 2. 지수(제곱할 횟수) 입력 받기
    try:
        exp_str = input("Enter exponent: ")
        # 입력받은 문자열을 정수(int)로 변환
        exponent = int(exp_str)
    except ValueError:
        # 정수로 변환할 수 없을 경우 예외 처리
        print("Invalid exponent input.")
        return # 프로그램 종료

    # 3. 제곱 계산 (반복문 사용)
    result = 1.0 # 초기 결과값을 1.0으로 설정 (어떤 수의 0제곱은 1)

    # 지수가 양수인 경우만 계산
    if exponent >= 0:
        for _ in range(exponent): # 지수만큼 반복
            result *= number # result = result * number 와 같은 의미
    else:
        # 지수가 음수인 경우 (예: 2의 -2제곱 = 1 / (2의 2제곱))
        # 먼저 양수 지수로 계산한 후 역수를 취함
        for _ in range(abs(exponent)): # 지수의 절대값만큼 반복
            result *= number
        result = 1.0 / result # 역수 계산

    # 4. 결과 출력
    # float()으로 형변환 했기 때문에 결과도 float 형태로 나오므로
    # .0이 붙을 수 있습니다 (예: 81.0).
    # 과제 요구사항에 따라 81처럼 정수로 나오게 하고 싶다면 int()로 한 번 더 감싸주면 됩니다.
    # 여기서는 float 형태로 출력합니다.
    print(f"Result: {result}")

if __name__ == "__main__":
    main()