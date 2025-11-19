cpf = input("Enter first nine digits(just int number and no spaces): ")
multi_1 = 10
multi_2 = 11
j = 0
k = 0
sum_total_1 = 0
sum_total_2 = 0
for i in cpf:
    cpf_number_1 = int(cpf[j])
    verifier_1 = cpf_number_1 * multi_1
    j += 1
    multi_1 -= 1
    sum_total_1 += verifier_1
    rest_1 = (sum_total_1 * 10) % 11
    if rest_1 > 9:
        first_digit = 0
    if rest_1 < 9:
        first_digit = rest_1
rest_str = str(rest_1)
cpf += rest_str
for i in cpf:
    cpf_number2 = int(cpf[k])
    k += 1
    verifier_2 = cpf_number2 * multi_2
    multi_2 -= 1
    sum_total_2 += verifier_2
    rest_2 = (sum_total_2 * 10) % 11
    if rest_2 > 9:
        second_digit = 0
    if rest_2 < 9:
        second_digit = rest_2
rest_str_2 = str(rest_2)
cpf += rest_str_2

print(f"first digit: {rest_1}", f"and the second digit: {rest_2}", sep2="-")
print(f"the full cpf is: {cpf}")
