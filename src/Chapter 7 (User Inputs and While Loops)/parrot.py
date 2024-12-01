# the input function pauses your program and
# waits for the user to enter some text
# ask the user to enter some text then display it back to the user
# message = input("How old are you? ")
# print(f"You are {message} years old.")

prompt = "\nTell me something and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# create a flag called 'active'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)