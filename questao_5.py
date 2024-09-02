str = input()

str_inversa = ''
for i in range(len(str), 0, -1):
    str_inversa += str[i-1]

print(str_inversa)