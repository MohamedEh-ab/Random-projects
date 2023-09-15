# the program does the mathematical operation for the user to convert decimal-format integers to hexadecimal format
import os, time

def convertTuple(tup): # a function used later to take the items of the resultant tuple and join them together to form a readable string for the user
    str = ''.join(tup)
    return str

while True: # for resetting the program
    prompt = int(input("Enter input in decimal format: "))
    x = [] # our empty list for the remainder which will be converted into hexadecimal 

    while prompt: 
        result = prompt / 16 # the input decimal is divided by 16
        remainder = (result) % 1.0 # then we take the fractional part of the result and store it as a "remainder"
        x.append(str(int(remainder * 16))) # we multiply the remainder by 16 so we can have our list items to convert it to hexadecimal
        prompt = int(result) # we take the integar part and repeat the process until the remainder = zero

    # hexadata.txt contains the following data that will be used in converting process:
    # 15=F
    # 14=E
    # 13=D
    # 12=C
    # 11=B
    # 10=A
    # 9=9
    # 8=8
    # 7=7
    # 6=6
    # 5=5
    # 4=4
    # 3=3
    # 2=2
    # 1=1
    # 0=0

    hexadata = {}
    # os.chdir(r'C:\Users\Mohamed\OneDrive\Desktop\New folder') <--- the absolute path to my folder where the txt file
    with open("hexadata.txt") as f:
        for line in f:
            key, value = line.split('=')
            hexadata[key.strip()] = value.strip()

    y = [] # our list for the hexadecimal items after converting process is completed

    for i in x: # a for loop that replaces each item in our original remainder list according to the data from our txt file to convert it into hexadecimal format
        char = hexadata[i]
        y.append(str(char))

    y = tuple(y) # we convert our list to tuple so we can join its items together in a single string

    z = convertTuple(y) # this function is defined earlier for joining purpose and z here contains our hexadecimal format at last


   # this just a cool waiting thing to stimulate calculating process in professional calculators
    print("")
    print("Please wait")
    for i in range(2):
        print(".", end="", flush=True)
        time.sleep(1)

    print("")
    print("")
    print("Your input in hexadecimal format: " + z) # here is our output. don't mind the annoying print sentences, I grew bored and tired from constant bug fixing till this point ;( 
    print("----------------------------------------------")
    print("")