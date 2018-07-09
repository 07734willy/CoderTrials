
def encode(num):
	codeword = "1"
	fibs = [1, 2]
	while fibs[-1] < num:
		fibs.append(fibs[-1]+fibs[-2])
	fibs.pop()
	while fibs:
		if fibs[-1] <= num:
			num -= fibs[-1]
			codeword += "1"
		else:
			codeword += "0"
		fibs.pop()
	return codeword[::-1]

def decode(code):
	code += "1"
	fibs = [1, 2]
	val = 0
	for i, c in enumerate(code):
		if c == "1":
			val += fibs[i]
		fibs.append(fibs[-1]+fibs[-2])
	return val


if __name__ == "__main__":
	string = input()

	if len(string) > 1 and string[:2] == "0b":
		print("".join(map(chr,map(decode,string[2:].split("11")[:-1]))))
	else:
		print("0b"+"".join(map(encode,map(ord,string))))
