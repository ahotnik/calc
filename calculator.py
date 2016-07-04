a = float(input("The a number:"))
b = float(input("The b number:"))

calculate = {
	'+': a+b,
	'-': a-b,
	'*': a*b
}

operation = str(input("The operation: "))

if operation == '/' and b != 0:
	calculate['/'] = a/b

calculate.setdefault(operation, "Error operation")

print(calculate[operation])