
print("****************************************")
print()
print("Your string can only contain letters")
print()

choice = input("Do you want to start? yes/no: ")

a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=s=v=w=x=y=z=0

if  choice.upper() == "YES":

	word = input("Enter a string: ")

	for letter in word:
		if letter.upper() == "A" :
			a = a + 1
		elif letter.upper() == "B" :
			b = b + 1
		elif letter.upper() == "C" :
			c = c + 1
		elif letter.upper() == "D" :
			d = d + 1
		elif letter.upper() == "E" :
			e = e + 1
		elif letter.upper() == "F" :
			f = f + 1
		elif letter.upper() == "G" :
			g=g+1
		elif letter.upper() == "H" :
			h=h+1
		elif letter.upper() == "I" :
			i=i+1
		elif letter.upper() == "J" :
			j=j+1
		elif letter.upper() == "K" :
			k=k+1
		elif letter.upper() == "L" :
			l=l+1
		elif letter.upper() == "M" :
			m=m+1
		elif letter.upper() == "N" :
			n=n+1
		elif letter.upper() == "O" :
			o=o+1
		elif letter.upper() == "P" :
			p=p+1					  
		elif letter.upper() == "Q" :
			q=q+1
		elif letter.upper() == "R" :
			r=r+1
		elif letter.upper() == "S" :
			s=s+1
		elif letter.upper() == "T" :
			t=t+1
		elif letter.upper() == "U" :
			u=u+1
		elif letter.upper() == "V" :
			v=v+1
		elif letter.upper() == "W" :
			w=w+1
		elif letter.upper() == "X" :
			x=x+1
		elif letter.upper() == "Y" :
			y=y+1
		elif letter.upper() == "Z" :
			z=z+1	
		else:
			print("Only letters are allowed in the string ")
			
	if a > 0 :
		print("a = " + str(a))
	if b > 0 :
		print("b = " + str(b))
	if c > 0 :
		print("c = " + str(c)) 
	if d > 0:
		print("d = " + str(d)) 
	if e > 0 :
		print("e = " + str(e)) 
	if f > 0 : 
		print("f = " + str(f)) 
	if g > 0 : 
		print("g = " + str(g)) 
	if h > 0 : 
		print("h = " + str(h)) 
	if i > 0 : 
		print("i = " + str(i)) 
	if j > 0 :
		print("j = " + str(j)) 
	if k > 0 :
		print("k = " + str(k)) 
	if l > 0 :
		print("l = " + str(l)) 
	if m > 0 : 
		print("m = " + str(m)) 
	if n > 0 : 
		print("n = " + str(n)) 
	if o > 0 :
		print("o = " + str(o)) 
	if p > 0 :
		print("p = " + str(p)) 
	if q > 0 :
		print("q = " + str(q)) 
	if r > 0 :
		print("r = " + str(r)) 
	if s > 0 : 
		print("s = " + str(s)) 
	if t > 0 :
		print("t = " + str(t)) 
	if u > 0 :
		print("u = " + str(u)) 
	if v > 0 : 
		print("v = " + str(v))
	if w > 0 :
		print("w = " + str(w))
	if x > 0 :
		print("x = " + str(x)) 
	if y > 0 :
		print("y = " + str(y))
	if z > 0 : 
		print("z = " + str(z)) 
else:
	print()
	print("The end")
	


	
	
