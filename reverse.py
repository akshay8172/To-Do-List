'''original_string = "malayalam"

reversed_string = "" 

for i in range(len(original_string) - 1, -1, -1):

    reversed_string += original_string[i]

if original_string == reversed_string:

    print("It's palindrome")

else:

    print("Not Palindrome")
    

num1 = 10

num2 = 20

sum = num1 + num2

print(sum)

'''
string = "amma"
string = string.lower()
n = len(string)
print(n)
for i in range(n // 2):
    if string[i] != string[n - 1 - i]:
        print(f"{string} is not a palindrome.")
        break
else:
    print(f"{string} is a palindrome.")

