def question_page():
	return open('question_page.html','r').read()

def calling():
	return open('youtube.html','r').read()

def one_line_answer(statement, n):
	return open('one_line_answer.html','r').read().replace('|statement|', statement).replace("|n|", str(n))

def error_page():
	return open('error_page.html','r').read()

def making_list(statement, var_lst):
	var3 = open('making_list.html','r').read().replace('||statement||', statement)
	for i in var_lst:
		var3 += "<font size = 10>" "<li>" + str(i) + "</li>" "</font>"
		
	var3 += "</ul>" + \
	"</body>" + \
	"</html>"
	return var3

def is_prime(num):
	isprime = True
	for i in range(2,num):
		if (num%i) == 0:
			isprime = False
			break
	if isprime == True:
		return isprime
	else:
		return False

def prime(number):
	x = [ ]
	index = 2
	while index <= number:
		a = is_prime(index)
		if a == True:
			x.append(index)
		index = index + 1
	return x

def squares(number):
	if number == 0:
		return 0
	else:
		return number**2

def cubes(number):
	if number == 0:
		return 0
	else:
		return number**3

def recursive_sum(number):
	if number == 0:
		return 0
	else:
		return number + recursive_sum(number - 1)

def recursive_sum_of_cube(number):
	if number == 0:
		return 0
	else:
		return (number**3 + recursive_sum_of_cube(number-1))

def recursive_sum_of_square(number):
	if number == 0:
		return 0
	else:
		return (number**2 + recursive_sum_of_square(number-1))

def factorial_recursive(number):
	if number == 0:
		return 1
	else:
		return number * factorial_recursive(number - 1)

def sum_of_factorial_recursive(number):
	if number == 0:
		return 0
	else:
		return factorial_recursive(number) + sum_of_factorial_recursive(number-1)


