def main():
    user_input = input("숫자들을 공백으로 구분하여 입력하세요: ")

    # 1. 입력값이 비어 있는지 확인
    if not user_input:
        print("Invalid input.")
        return

    # 2. 공백으로 구분된 문자열을 리스트로 변환
    input_str_list = user_input.split()

    numbers = []
    # 3. 각 문자열을 숫자로 변환하고 예외 처리
    for item in input_str_list:
        try:
            numbers.append(float(item)) # float()로 실수(소수점 있는 숫자)로 변환
        except ValueError: # 숫자로 변환할 수 없는 값이 있다면
            print("Invalid input.")
            return # 프로그램 종료

    # 4. 정렬 알고리즘 구현 (버블 정렬 예시)
    n = len(numbers)
    for i in range(n):
        # i번째 이후의 요소들을 확인하여 정렬
        for j in range(0, n - i - 1):
            # 현재 요소가 다음 요소보다 크면 위치를 바꾼다 (오름차순)
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # 두 숫자의 위치를 바꿈

    # 5. 정렬된 숫자들을 출력 형식에 맞게 출력
    # 숫자들을 문자열로 변환하면서 소수점 형태로 유지
    sorted_numbers_str = [f"{num:.1f}" for num in numbers] # .1f는 소수점 첫째 자리까지 표시
    # f"{num:.1f}"는 f-string이라는 문법으로, 변수를 문자열 안에 쉽게 넣을 수 있게 해줘요.
    # num:.1f는 숫자를 소수점 첫째 자리까지 표시하라는 의미예요.

    print("Sorted:", " ".join(sorted_numbers_str))


if __name__ == "__main__":
    main()