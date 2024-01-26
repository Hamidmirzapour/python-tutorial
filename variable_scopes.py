""""
This module practice working with variable scopes.
LEGB
Local, Enclosing, Global, Built-in
First, Check Local variables, then Enclosing, Global and Builtin Variables
"""

x = "global x"

def test(z):
    # global x  ==> Make x in function global and access to it from outside the function
    # x = "local x"
    print(x) # Check if there is local x defined in function and show it, if there isn't local variable check for outer variable (Enclosing), then global one
    print(z)

test("local z")
print(x) # Check if there is global variable and then builtin and if both not available, give NameError: name 'x' is not defined


# Enclosing
def outer():
    outer = 'Outer'
    def inner():
        nonlocal inner # Make variable accessible outside inner function enclosed
        inner = 'Inner'
        print(inner)
        print(outer)
    inner()
    print(outer)
outer()

# Show all reserved builtin variables
import builtins
print(dir(builtins))