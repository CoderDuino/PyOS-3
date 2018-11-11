import time

print("\033c")

def table(rows, columns):
	for i in range(1, int(rows) + 1 ):
		print("\t", i)

	print("\n\n")

	for i in range(1, int(columns) + 1 ):
		print(i, end="")
		for j in range(1, int(rows) + 1 ):
			print ("\t",i*j,end="")
		print("\n\n")
		
table(10, 10)
time.sleep(5)
# print("\033c")