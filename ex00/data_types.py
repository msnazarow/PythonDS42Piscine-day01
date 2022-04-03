
def main():
	a = 1
	b = '1'
	c = 1.
	d = True
	e = [1]
	f = {1: 1}
	g = (1,)
	h = {1}

	print(list(map(lambda x: type(x).__name__, [a, b, c, d, e, f, g, h])))

if __name__ == '__main__':
	main()