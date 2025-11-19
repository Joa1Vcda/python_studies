"""Prints,Arguments and strings"""

print(12, 34, 72, sep="-", end="\r\n")
print(56, 78, sep="-")
# sep is used to separate elements in print
# end is used to add elements,but i can broke(with \r\n) a line or bring togheter the next line(with "")
print("Hello World")
print("Hello 'World")
# "\" is for escape,single quotes will not brake the code because "\" will consider a sting element
print("Hello World")
print(r"He\'llo \'Worl\'d")
# r will consider all elements in the print
print('Hello "World"')
# "" is funcional in a print if the print use single quotes
print(1, "Hello World")
