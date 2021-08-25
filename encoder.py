fib = [1, 1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

def c2f(c):
	n = ord(c)
	b = ''
	for i in range(10, -1, -1):
		if n >= fib[i]:
			n -= fib[i]
			b += '1'
		else:
			b += '0'
	print(b)
c2f('a')

def f2c(a):
    b=[]
    for i in range(32,127):
        b+= chr(a)
    print(b)

f2c(10000100000)
#flag = open('flag.txt', 'r').read()
#enc = ''
#for c in flag:
#	enc += c2f(c) + ' '
#with open('flag.enc', 'w') as f:
#	f.write(enc.strip())