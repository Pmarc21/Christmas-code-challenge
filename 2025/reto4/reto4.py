santa_code = "[1++][2-][3+][<]"
INIT_COUNTER = '['
END_COUNTER = ']'
def decode_santa_pin(code: str) -> str:
    last_digit = 0
    sum_total = 0
    for char in code:
        if char == INIT_COUNTER or char == END_COUNTER:
            sum_total = 0
        if char.isdigit():
            sum_total += int(char)
            last_digit = int(char)
        else:
            if char == '+':
                sum_total += 1
            elif char == '-':
                sum_total -= 1
            else:
                sum_total += last_digit
        if sum_total > 10:
            sum_total = sum_total % 10
    final_string = "".join(str(sum_total))
    return final_string

print(decode_santa_pin(santa_code))