"""while/break/continue"""

# attribution operators
# =     +=      -=      *=      /=      //=     %=

"""loop"""
condition = True

while condition:
    name = input("Enter your name: ")
    print(f"your name is {name}")
    if name == "sair":
        break

"""counter"""
counter = 0

while counter < 40:
    counter += 1

    if counter == 6:
        continue

    if counter >= 12 and counter <= 27:
        print("I will not show the", counter)
        continue

    print(counter)
counter = 0

while counter < 40:
    counter += 1

    if counter == 6:
        continue

    if counter >= 12 and counter <= 27:
        print("I will not show the", counter)
        continue

    print(counter)

number_of_rows = 5
number_of_columns = 5

row = 1

while row <= number_of_rows:
    column = 1
    while column <= number_of_columns:
        print(f"{row=},{column=}")
        column += 1
    row += 1

"""intering strings with while"""

NAME = "João Vitor"
new_name = ""
start = 0

while start < len(NAME):
    new_name += f"*{NAME[start]}"
    start += 1

print(new_name)
