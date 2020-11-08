#exercise 4
integer = int(input())
if str(integer) == str(integer)[::-1] and integer >= 10:
    print("Integer is symmetric")
else:
    print("Integer is not symmetric")