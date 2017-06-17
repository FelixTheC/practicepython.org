#! /usr/env/python3

def fib(maximum):
	a = 1
	b = 0
	fib_list = []
	while b < maximum:
		a,b = b, b+a
		fib_list.append(b)
	return fib_list
	
	
if __name__ == "__main__":
	print(fib(100))
