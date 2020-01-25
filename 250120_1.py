t_user = input("input temperature: ")
c_or_f = input("if celsius input 'C', else 'F': ")
t_input = c_or_f + t_user

if "C" in t_input:
	print(int(t_user) * 1.8 + 32)
else:
	print((int(t_user)-32) / 1.8)
	
