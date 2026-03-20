prompt = "\nPlease enter something and I repeat it"
prompt += "\n(Enter 'quit' when you are finished.) "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


    