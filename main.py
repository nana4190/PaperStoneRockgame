import random

# function for generating system values
def cpu_select():
    mylist = ['R', 'S', 'P']
    return random.choice(mylist)

word = input("Please Pick an option either 'R', 'P' or 'S': ").upper()
dict = {
  'R': "Rock",
  'P': "Paper",
  'S': "Scissors"
}

validate = bool(1)
while validate:
    if word != 'R' and word != 'P' and word != 'S':
        print("Error!!! Try Again.")
        word = input("Please input either 'R', 'P' or 'S': ").upper()
    else:
        # calling System to randomly pick its own value
        cpuValue = cpu_select()
        print("Player", "(",dict[word],")", ":", "CPU", "(",dict[cpuValue],")")
        if cpuValue == word:
            print("A TIE!!! Guess Another: ")
            word = input("Input either 'R', 'P' or 'S': ").upper()
        elif (word == 'R' and cpuValue == 'S') or (word == 'P' and cpuValue == 'R') or (word == 'S' and cpuValue == 'P'):
            print("Player Won!!!")
            validate = bool(0)
        elif (cpuValue == 'R' and word == 'S') or (cpuValue == 'P' and word == 'R') or (cpuValue == 'S' and word == 'P'):
            print("CPU Won")
            validate = bool(0)