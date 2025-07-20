# minmax_calculator.py

def main():
    print("숫자들을 입력하세요 (공백으로 구분):")
    user_input = input()
    num_strings = user_input.split()
    
    numbers = []
    
    for s in num_strings:
        try:
            num = float(s)
            numbers.append(num)
        except ValueError:
            print("Invalid input.")
            return
            
    if not numbers:
        print("No numbers entered.") # 또는 요구사항에 맞게 처리
        return

    # --- 여기서부터 최소값/최대값 찾는 로직 시작 ---
    
    # 첫 번째 숫자를 일단 최소값과 최대값으로 가정
    min_value = numbers[0] 
    max_value = numbers[0]
    
    # 두 번째 숫자부터 마지막 숫자까지 반복하며 비교
    for i in range(1, len(numbers)): # numbers 리스트의 인덱스 1부터 끝까지 반복
        current_num = numbers[i] # 현재 보고 있는 숫자
        
        if current_num < min_value: # 현재 숫자가 현재까지의 최소값보다 작으면
            min_value = current_num # 최소값을 현재 숫자로 업데이트
        
        if current_num > max_value: # 현재 숫자가 현재까지의 최대값보다 크면
            max_value = current_num # 최대값을 현재 숫자로 업데이트
            
    # --- 최소값/최대값 찾는 로직 끝 ---

    print(f"Min: {min_value:.1f}, Max: {max_value:.1f}") # 결과 출력 (소수점 첫째 자리까지)

if __name__ == "__main__":
    main()