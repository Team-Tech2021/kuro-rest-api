def nth_fib(n):
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return nth_fib(n-1) + nth_fib(n-2)