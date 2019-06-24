prompt = "How old are you? "
prompt += "\nInput your age and I will calculate your cost: "


while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Tickets are free for " + str(age) + " year olds.\n")
    elif int(age) < 12:
        print("Tickets are $10 for " + str(age) + " year olds.\n")
    else:
        print("Tickets are $15 for " + str(age) + " year olds.\n")
    
