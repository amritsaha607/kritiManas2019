import matplotlib.pyplot as plt

def eqn(x):
	# f(x) = 0
	return x**3-7*x+1

def solve():
	x = 0
	step = 0.001
	err = 1000
	count = 0
	while(err>0.001):
		curr_err = abs(eqn(x))
		print('current error : ' + str(curr_err))
		plt.plot(x, curr_err, 'o')
		if curr_err<=0.001:
			print('solved !')
			return x
		if ((abs(eqn(x-step)) < curr_err) or (abs(eqn(x-step)) < abs(eqn(x+step)))):
			x -= step
		else:
			x += step
		count += 1
		if count==20000:
			print('Oops ! Could not solve !')
			return

sol = solve()
if sol: 
	print('Root : ' + str(sol))
plt.show()