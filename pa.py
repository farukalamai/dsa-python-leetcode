# sen = "my name is faruk"

# def is_consonant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# consonats = [i for i in sen if is_consonant(i)]

# print(consonats)

my_list = [-1, 10, -20, 2, -90, 60, 23, 10]

def get_number(num):
    if num > 0:
        return num
    else:
        return "negative number"
new_list = [get_number(i) for i in my_list]

print(new_list)

# my_list = [1,2,3,4]
# new_list = []
# for i in my_list:
#     mul = i*2
#     new_list.append(mul)

# print(new_list)