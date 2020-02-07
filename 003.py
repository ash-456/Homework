user_input = input()

a = user_input.find(" not")

b = user_input.find(" poor")

if b > a and a > 0 and b > 0:

	print(user_input.replace(user_input[a: b + 5], " good"))



