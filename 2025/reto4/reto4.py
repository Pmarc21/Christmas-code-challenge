santa_code = "[9+][0-][4][<]"
def decode_santa_pin(code: str) -> str:
    last_digit = 0
    sum_total = 0
    INIT_COUNTER = '['
    END_COUNTER = ']'
    array_numbers = []
    code_aux = code.split('][')
    print(code_aux)
    for i in range(len(code_aux)):
        if code_aux[i] == INIT_COUNTER:
            sum_total = 0
        elif code_aux[i] == END_COUNTER:
            array_numbers.append(sum_total)
        elif code_aux[i].isdigit():
            sum_total += int(code_aux[i])
            last_digit = sum_total
        else:
            if code_aux[i] == '+':
                sum_total += 1
                last_digit = sum_total
            elif code_aux[i] == '-':
                sum_total -= 1
                last_digit = sum_total
            elif code_aux[i] == '<':
                sum_total += last_digit
        if sum_total >= 10:
            sum_total = sum_total % 10
    if len(array_numbers) > 3:
        final_string = "".join(str(x) for x in array_numbers)
        return final_string
    else:
        return None

print(decode_santa_pin(santa_code))