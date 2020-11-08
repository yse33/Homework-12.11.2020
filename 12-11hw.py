#exercise 1
num = int(input()) 
count = int(input())
original_num = num
i = 0
while i < count:
    i += 1
    print(num)
    num += original_num


#exercise 2
str1 = str(input())
vowels = "AaEeIiOoUu"
vowel_count = 0
for i in vowels:
    for y in str1:
        if i in y:
            vowel_count += 1
print(vowel_count)

#exercise 3
list = ["my", 1, "turtle", "explain", 3.14] 
for i in list:
    if isinstance(i, int) or isinstance(i, float):
        list.remove(i)
print(list)

#exercise 4
integer = int(input())
if str(integer) == str(integer)[::-1]:
    print("Integer is symmetric")
else:
    print("Integer is not symmetric")