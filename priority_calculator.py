# calculator.py (가정)에서 재사용할 연산 함수들
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero.") # 0으로 나눌 경우 예외 발생
    return a / b

# -- 여기서부터 priority_calculator.py의 메인 로직 --

def main():
    user_input = input("수식을 입력하세요 (예: 4 + 5 * 3 - 2): ")

    if not user_input.strip(): # 입력이 비어있는지 확인 (공백만 있는 경우도 포함)
        print("Invalid input.")
        return

    # 1. 입력 문자열을 공백 기준으로 분리
    tokens = user_input.split()
    
    # 2. 숫자와 연산자 유효성 검사 및 숫자 변환
    # 숫자는 float으로, 연산자는 + - * / 인지 확인
    processed_tokens = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            processed_tokens.append(token)
        else:
            try:
                processed_tokens.append(float(token))
            except ValueError:
                print("Invalid input.")
                return

    # 모든 토큰이 유효한지 확인 (예: 1 + + 2 같은 경우)
    if not is_valid_expression(processed_tokens):
        print("Invalid input.")
        return
        
    # 3. 곱셈과 나눗셈 먼저 처리 (우선순위 1)
    # 임시 리스트를 사용하여 연산 결과를 저장
    temp_list = []
    i = 0
    while i < len(processed_tokens):
        if processed_tokens[i] == '*':
            # 이전 숫자와 현재 숫자를 곱함
            # temp_list의 마지막 요소가 이전 숫자이므로 pop()으로 꺼내고,
            # 다음 요소 (processed_tokens[i+1])가 현재 숫자
            try:
                result = multiply(temp_list.pop(), processed_tokens[i+1])
                temp_list.append(result)
                i += 2 # 연산자(*)와 다음 숫자 건너뛰기
            except IndexError: # 연산자 뒤에 숫자가 없는 경우
                print("Invalid input.")
                return
            except ValueError as e: # 0으로 나누는 경우 등
                print(f"Error: {e}")
                return
        elif processed_tokens[i] == '/':
            try:
                result = divide(temp_list.pop(), processed_tokens[i+1])
                temp_list.append(result)
                i += 2 # 연산자(/)와 다음 숫자 건너뛰기
            except IndexError:
                print("Invalid input.")
                return
            except ValueError as e:
                print(f"Error: {e}")
                return
        else: # 숫자나 덧셈/뺄셈 연산자는 일단 temp_list에 추가
            temp_list.append(processed_tokens[i])
            i += 1
    
    # 4. 덧셈과 뺄셈 처리 (우선순위 2)
    # 곱셈/나눗셈 결과로 구성된 temp_list를 사용하여 덧셈/뺄셈 수행
    # temp_list의 첫 번째 요소가 시작 숫자가 됨
    if not temp_list: # 입력이 숫자 하나만 있는 경우 (예: 5)
        print("Invalid input.")
        return

    result = temp_list[0]
    i = 1
    while i < len(temp_list):
        operator = temp_list[i]
        operand = temp_list[i+1] # 다음 피연산자 (숫자)
        
        if operator == '+':
            result = add(result, operand)
        elif operator == '-':
            result = subtract(result, operand)
        else: # 연산자가 +,-가 아닌 경우 (잘못된 입력 처리)
            print("Invalid input.")
            return
        i += 2 # 연산자와 다음 숫자 건너뛰기

    print(f"Result: {result:.1f}") # 소수점 첫째 자리까지 출력

# 입력 토큰의 유효성을 검사하는 헬퍼 함수
def is_valid_expression(tokens):
    if not tokens:
        return False
    
    # 첫 번째와 마지막 토큰은 숫자여야 함
    if not isinstance(tokens[0], (int, float)) or not isinstance(tokens[-1], (int, float)):
        return False

    # 숫자-연산자-숫자 패턴 확인
    for i in range(len(tokens)):
        if i % 2 == 0: # 짝수 인덱스는 숫자여야 함
            if not isinstance(tokens[i], (int, float)):
                return False
        else: # 홀수 인덱스는 연산자여야 함
            if not isinstance(tokens[i], str) or tokens[i] not in ['+', '-', '*', '/']:
                return False
    
    return True

if __name__ == "__main__":
    main()