# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
count = 0

while(1) :
	user_input = input("Enter two numbers : ")
	a = int(user_input.split()[0])
	b = int(user_input.split()[1])
	if a==0 and b==0 :
		print("Entering count : {0}".format(count))
		break
	else :
		if a>b:
			a,b = b,a
		for i in range(a,b+1):
			if i%3==0:
				print(i, end=' ')
		print()
		count += 1