# 덧셈 함수
def add(a, b):
    return a + b

# 뺄셈 함수
def subtract(a, b):
    return a - b

# 곱셈 함수
def multiply(a, b):
    return a * b

# 나눗셈 함수
def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero.")
    return a / b

# 수식 파싱 및 계산 함수 추가
def calculate_expression(expression):
    # 공백을 기준으로 문자열을 분리 (예: "2 + 3" -> ["2", "+", "3"])
    parts = expression.split()

    # 입력 형식 검증
    if len(parts) != 3: # "숫자 연산자 숫자" 형태여야 하므로 길이가 3이 아니면 오류
        raise ValueError("Invalid expression format. Use 'number operator number' (e.g., 2 + 3).")

    try:
        num1 = float(parts[0]) # 첫 번째 부분을 숫자로 변환
        operator = parts[1]    # 두 번째 부분은 연산자
        num2 = float(parts[2]) # 세 번째 부분을 숫자로 변환
    except ValueError:
        raise ValueError("Invalid number input in expression.") # 숫자 변환 오류

    result = 0
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2) # 0으로 나누는 예외는 divide 함수에서 처리됨
    else:
        raise ValueError("Invalid operator.") # 허용되지 않는 연산자

    return result

# 메인 함수 (수식 입력 방식으로 변경)
def main():
    while True:
        try:
            # 사용자로부터 수식 입력 받기
            expression = input("Enter expression: ")

            # 수식 계산 함수 호출
            calculated_result = calculate_expression(expression)

            # 결과 출력
            print(f"Result: {calculated_result}")
            break # 올바르게 계산이 완료되면 반복문 종료

        except ValueError as e:
            print(e) # 예외 메시지 출력
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()