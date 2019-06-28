sandwich_orders = ['ham', 'pastrami', 'pastrami', 'jelly', 'club', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    production = sandwich_orders.pop()
    
    print("Making your " + production + " sandwich now!")
    
    finished_sandwiches.append(production)

for finished_sandwich in finished_sandwiches:
    print("\nYour " + finished_sandwich + " sandwich is finished!")
    
print("\n\nIn Total:")

for finished_sandwich in finished_sandwiches:  
    print(finished_sandwich)
