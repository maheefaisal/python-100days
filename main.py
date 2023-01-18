# f = open('mahee.txt','r')
# text = f.read()
# print(text)

# f.close()
# f = open('mahee.txt','a')
# f.write('Maahee')
# f.close()

with open('mahee.txt','a') as f:
    f.write("mahee is awesome")