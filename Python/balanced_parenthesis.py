# Codingame problem :
# Check if the parenthesis are closed in input

parenthesis = {
		"(" : ")",
		"{" : "}",
		"[" : "]"
	}

def	get_corresponding_key(value):
	return list(parenthesis.keys())[list(parenthesis.values()).index(value)]

if __name__ == "__main__":
	line = input()

	stack = list()
	for char in line:
		if char in parenthesis.keys():
			stack.append(char)
		if char in parenthesis.values():
			if not len(stack):
				break
			else:
				if stack[-1] != get_corresponding_key(char):
					break
				else:
					# By default without the index argument given, the argument defaults to -1
					stack.pop()

	print("Balanced" if not len(stack) else "Not Balanced")
