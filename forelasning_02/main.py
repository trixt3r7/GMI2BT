
# Modifiera lista i en funktion (slide 17)
def print_designs(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_designs.append(current_design)


def show_printed_designs(completed_designs):
    for design in completed_designs:
        print(design)


unprinted_designs = ['Star destroyer', 'Millenium falcon', 'X-wing', 'B-wing', 'A-Wing']
printed_designs = []
print('\nUnprinted designs')
print_designs(unprinted_designs, printed_designs)
print('\nPrinted designs')
show_printed_designs(printed_designs)

print()
# Okänt antal parametrar (slide 18)
def make_pizza(*topping):
    print(topping)


make_pizza("Skinka")
make_pizza("Skinka", "Ost", "Lök", "Svamp")
