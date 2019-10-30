import numpy as np

def fun(x, y):
	return np.exp(-(x*x+y*y))

def decode(chromosome):
	x, y = 0,0
	for i in range(len(chromosome)//2):
		x += chromosome[i]*2**(-(i+1))
		y += chromosome[i+10]*2**(-(i+1))
	return (-3+6/(1-1/1024)*x, -3+6/(1-1/1024)*y)

def crossover_and_mutate(chromosome1, chromosome2, p_mut, p_cross):
	if np.random.rand(1) > p_cross:
		return (chromosome1, chromosome2)
	else:
		crossover_point = np.random.randint(1,19)
		c1 = np.concatenate((chromosome2[:crossover_point], chromosome1[crossover_point:]))
		c2 = np.concatenate((chromosome1[:crossover_point], chromosome2[crossover_point:]))
		
		c1 = np.array( [(x+1)%2 if np.random.rand(1) <= p_mut else x for x in c1] )
		c2 = np.array( [(x+1)%2 if np.random.rand(1) <= p_mut else x for x in c2] )

		return(c1, c2)

## population size 10 and chromosome length 20
gen_old = np.random.randint(2, size = (10, 20))
gen_new = np.zeros((10,20))
fit_vals_old = np.zeros(10)

for i in range(30):

	for i, chromosome in enumerate(gen_old):
		x, y = decode(chromosome)
		fit_vals_old[i] = fun(x,y)

	elit = np.argmax(fit_vals_old) ##perform elitism, i.e keep 2 copies of best individial for next generation
	gen_new[8] = gen_old[elit]
	gen_new[9] = gen_old[elit]

	for i in range(4):
		pair = np.random.choice(10, 2, p = fit_vals_old/np.sum(fit_vals_old))
		chromosome1 = gen_old[pair[0]]
		chromosome2 = gen_old[pair[1]]

		(chromosome1, chromosome2) = crossover_and_mutate(chromosome1, chromosome2, 0.1, 0.75)
		gen_new[2*i] = chromosome1
		gen_new[2*i+1] = chromosome2

	gen_old = np.copy(gen_new)
	print(np.max(fit_vals_old))





