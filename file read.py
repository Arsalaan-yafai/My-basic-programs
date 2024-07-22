a= open("arsalaan.txt","r+")
c= a.write("yafai bolte aando\n")
b= a.read()

print(b)
print(a.readline())

a.close()
"""
print(a.readlines())

for line in a:
    print(line, end="")

print(a.readline())
print(a.readline())
print(a.readline())
"""