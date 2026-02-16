#What is the output of this code?

def fun(*args, **kwargs):
    for key, value in kwargs.items():
        print(f'{value}: {key}')
    for arg in args:
        print(arg)
fun("COP3502C", "Prog 1", lab="Cows")