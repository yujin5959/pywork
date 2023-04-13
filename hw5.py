def read_single_digit(digit):
    """
    한 자리 10진 정수에 대한 한글 문자열을 반환하는 함수
    """
    digit_names = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digit_names[digit]

def read_number(number):
    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    ones_digit = number % 10
    
    result = read_single_digit(hundreds_digit)+read_single_digit(tens_digit)+read_single_digit(ones_digit)
    
    return result

number = int(input("세 자리 정수 입력: "))

print(read_number(number))
