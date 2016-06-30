import os

x=os.getcwd()
print(x)
y=os.chdir(os.pardir) # mi hat het gnal

print(os.getcwd())

os.chdir(x)

print(os.getcwd())