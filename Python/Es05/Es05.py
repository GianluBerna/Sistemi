def push(stack, element):
    stack.append(element)
    return stack


def pop(stack):
    element = stack.pop()
    return stack, element


pila = [1, 2, 3, "ciao", "b"]

pila = push(pila, 6)
print(pila)

pila, _ = pop(pila)
print(pila)
