with open('mahee.txt', 'r') as f:
    f.seek(10)
    data = f.read(5)
    print(data)