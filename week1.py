print("Anything else")
# first test code
def print_hi(name, rep=1):
    if(rep!=1):
        print(f'Hello, {name}'*rep)
    else:
        print(f'Hello, {name}')

print_hi("World",8)
