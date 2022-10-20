import string

ls = [i * 10 for i in range(10)]
print(ls)

ls = [i * i for i in range(10)]
print(ls)

s ="qwertyuio"
ls = [i * 3 for i in s]
print(ls)


s ="qwertyuio"
STR = "qwe"
ls = [i in STR for i in s]
print(ls)

print(all(ls))
print(any(ls))

s ="qwe"
STR = "qwe"
ls = [i in STR for i in s]
print(ls)

print(all(ls))
print(any(ls))


s ="qwe"
STR = "qwe"
ls = [1, 2, 3]
print(ls)

print(all(ls))
print(any(ls))



# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(type(string.ascii_letters))
# print(string.hexdigits)
# print(string.octdigits)
# print(string.printable)
# print(string.punctuation)
# print(string.whitespace)