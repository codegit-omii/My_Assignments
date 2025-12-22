try:
    print("Reading File Content")
    with open("code\sample.txt", "r") as file:
        Line1 = file.readline()
        Line2 = file.readline()
        print("Line 1:", Line1)
        print("Line 2:", Line2)
        
except FileNotFoundError:
    print("Error: The File 'sample.txt' not found.")