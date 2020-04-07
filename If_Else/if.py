from prettytable import PrettyTable

x1 = PrettyTable()

code = open('if.txt','r')

lines = code.read().splitlines()
print('The Statement is :\n')
for i in lines:
  print('\t',i)

individual_lines = []

for entry in lines:
    x = []
    x = entry.split(" ")
    individual_lines.append(x)

goto,code1 = [],[]
for i in range(len(lines)):
	a = []
	if 'if' in lines[i]:
		a.append(lines[i])
		a.append('goto()')
		code1.append(a)
	elif 'return' in lines[i]:
		a.append('t1')
		a.append('=')
		a.append(individual_lines[i][-1][:len(individual_lines[i][-1])-1])
		code1.append(a)
		if('if' in lines[i-1]):
			code1.append(['goto()'])
		else:
			goto.append(len(code1))
	elif 'else' not in lines[i]:
		a.append(lines[i])
		code1.append(a)

goto.append(len(code1)+1)

for i in range(len(code1)):
	if 'if' in code1[i][0]:
		code1[i][0] = code1[i][0].replace('A<B','!A<B')

j=-1
for i in range(len(code1)):
	if 'goto()' in code1[i][0]:
		j+=1
		code1[i][0] = code1[i][0].replace('goto()','goto('+str(goto[j])+')')
	elif 'goto()' in code1[i][-1]:
		j+=1
		code1[i][-1] = code1[i][-1].replace('goto()','goto('+str(goto[j])+')')

x1.field_names = ['Index','Code']
for i in range(len(code1)):
	code2 = ""
	for j in code1[i]:
		code2 += j
	x1.add_row([i+1,code2])

x1.add_row([len(code1)+1,"END"])
print('\n\nThe Three Address Code Generated is :')
print(x1)