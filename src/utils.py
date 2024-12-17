import re

def validate_cpf(cpf):
    if not re.match(r"^\d{11}$", cpf):
        return False

    if cpf == cpf[0] * len(cpf):
        return False

    def calculate_digit(digits, multipliers):
        soma = sum(int(digit) * multiplier for digit, multiplier in zip(digits, multipliers))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    cpf_digits = cpf[:9]
    first_digit = calculate_digit(cpf_digits, range(10, 1, -1))
    cpf_digits += first_digit
    second_digit = calculate_digit(cpf_digits, range(11, 1, -1))
    return cpf.endswith(first_digit + second_digit)
