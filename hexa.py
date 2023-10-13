# the program does the mathematical operation for the user to convert decimal-format integers to hexadecimal format
# the program calculates remainders and append them in a list where theses remainders are then reversed by a function in order to output the hexadecimal format in right order
# the program then uses a dictionary loaded from a txt file where it tries to match the key items and replaces the values according to the dictionary
# then program appends the items after they have been replaced in another new list and then convert the list into tuple to join the items into one string
# the program outputs the desired output after a small wait thing that emulates calculation time without boring the user

import os, sys, subprocess, time

def convertTuple(tup):  # a function used later to take the items of the resultant tuple and join them together to form a readable string for the user
    str = ''.join(tup)
    return str


while True:  # for resetting the program
    try:
        prompt = int(input("Enter input in decimal format: "))
    except:
        print("insert only numbers, please.")
        time.sleep(3)
        os.system('clear')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    x = []  # our empty list for the remainder which will be converted into hexadecimal

    while prompt:
        result = prompt / 16  # the input decimal is divided by 16
        # remainder = (result) % 1.0
        # then we take the fractional part of the result and store it as a "remainder"
        remainder = prompt % 16
        # we multiply the remainder by 16 so we can have our list items to convert it to hexadecimal
        x.append(str(int(remainder)))
        # we take the integar part and repeat the process until the remainder = zero
        prompt = int(result)

    x = list(reversed(x))

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
    # using relative dir of txt file
    script_dir = os.path.dirname(__file__)
    rel_path = "hexadata.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path) as f:
        for line in f:
            key, value = line.split('=')
            hexadata[key.strip()] = value.strip()

    y = []  # our list for the hexadecimal items after converting process is completed

    for i in x:  # a for loop that replaces each item in our original remainder list according to the data from our txt file to convert it into hexadecimal format
        char = hexadata[i]
        y.append(str(char))

    # we convert our list to tuple so we can join its items together in a single string
    y = tuple(y)

    # this function is defined earlier for joining purpose and z here contains our hexadecimal format at last
    z = convertTuple(y)

   # this just a cool waiting thing to stimulate calculating process in professional calculators
    print("")
    print("Please wait")
    for i in range(2):
        print(".", end="", flush=True)
        time.sleep(1)

    print("")
    print("")
    # here is our output. don't mind the annoying print sentences, I grew bored and tired from constant bug fixing till this point ;(
    print("Your input in hexadecimal format: " + z)
    cont = input("\nProceed? ")
    if cont == "no":
        sys.exit()
        break
    else:
        os.system('clear')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    break