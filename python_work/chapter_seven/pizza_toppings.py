prompt = "Please enter your desired toppings."
prompt += "\nEnter 'quit' to finish your pizza: "

active = True
topping = ""
while active:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("I'll add some " + topping.lower() + "!\n")
