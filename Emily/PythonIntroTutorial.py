a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b

x=1
if x<0:
    x=0
    print("Negative changed to zero")
elif x==0:
    print("zero")
elif x==1:
    print("single")
else:
    print("more")


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w)<=6:
        words.insert(0, w)

print(words)

for i in range(5, 10, 3):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
        break
    else:
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

class MyEmptyClass:
    pass




# Provide default arguments
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'): # Prompt is unspecified - it is a keyword argument, and must be provided first in any call
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


# Shares the default with subsequent calls
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Wipe previous results from the function
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Cheeseshop sketch
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           "John Cleese",
           sketch="Cheese Shop Sketch")  ## nonkeyword arguments must all be before the keyword arguments

cheeseshop("Limburger")
cheeseshop("Brie", moral="Actually, we should not take moral lessons from cheese")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords.keys(): ## Not sorting the keyword arguments - now printed in the order in which specified in the function call
        print(kw, ":", keywords[kw])
