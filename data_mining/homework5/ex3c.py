

X1 = "GPAGFAGPPGAD"
X2 = "PRGDQGPVGRTG"
X3 = "GFPNFVDSVSDM"


def get_2_mers(X):
	list = []
	for i in range(0,len(X)-2):
		if X[i] == "G" and X[i+1] != "G" and X[i+2] != "G":
			list.append(X[i+1:i+3])
	return list


def string_kernel(X,Y):

	s1 = get_2_mers(X)
	s2 = get_2_mers(Y)
	sum = 0

	for x in s1:
		for y in s2:
			sum += 1
			sum += 1 if x[0] == y[0] else 0
			sum += 1 if x[1] == y[1] else 0
	return sum
	
print("k(X1,X2) = "+"{}".format(string_kernel(X1,X2)))
print("k(X1,X3) = "+"{}".format(string_kernel(X1,X3)))

