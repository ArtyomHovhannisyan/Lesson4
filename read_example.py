f=open('example.txt')

s=f.read(10)
print(s)

u=f.readline()
print(u)

y=f.read()
print(y)

f.close()

for line in open('example.txt'):
    if '3 lines' in line:
        print(line)




long=''
for Line in open('data.txt'):
    if len(Line)>len(long):
        long=Line
close('data.txt')
print(len(long))



f=open('example.txt')

f.write('A new massage for a new commit')

f.close()