def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"hello, {name}.")
    else:
        print("Error! It was not a name.")
greetings('Trent')
greetings('Alexder')
greetings()
greetings(24)