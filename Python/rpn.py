# Hackerrank challenge
# Reverse polish notation
# Example: ["2", "1", "+", "3", "*"] is equal to (2 + 1) * 3 , should output "6"

d = {
	'+' : lambda x, y : x + y,
	'-' : lambda x, y : x - y,
	'*' : lambda x, y : x * y,
	'/' : lambda x, y : x // y
}

if __name__ == "__main__":
	_input = input().split()
	stack = list()
	for elem in _input:
		if elem.isdigit():
			stack.append(elem)
		else:
			b = int(stack.pop())
			a = int(stack.pop())
			res = d[elem](a, b)
			stack.append(res)
	print(stack.pop())
