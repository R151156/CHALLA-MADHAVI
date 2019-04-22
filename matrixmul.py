a=input("enter the no of rows of m1:")
b=input("enter the no of columns of m1:")
c=input("enter the no of rows of m2:")
d=input("enter the no of columns of m2:")
if(b==c):
	x={ }
	i=0
	while(i<a):
		j=0
		while(j<b):
			x[i,j]=input("enter the elements")
			j=j+1
		i=i+1
	y={ }
	i=0
	while(i<c):
		j=0
		while(j<d):
			y[i,j]=input("enter the elements")
			j=j+1
		i=i+1
	z={ }
	i=0
	while(i<a):
		j=0
		while(j<d):
			z[i,j]=0
			k=0
			while(k<b):
				z[i,j]=z[i,j]+x[i,k]*y[k,j]
				k=k+1
			j=j+1
		i=i+1
	i=0
	while(i<a):
		j=0
		while(j<d):
			print z[i,j]
			j=j+1
		i=i+1	
else:
	print"matrix multiplication is not posiible"

    
             

          

    

           
