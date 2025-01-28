messages = ['hello world', 'i love python', 'happy new year']
sent_messages = []

print("Pending messages:")
print(messages)
def show_messages(messages):
    for message in messages:
        print(message.title())

# show_messages(messages)

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: '{current_message}'")
        sent_messages.append(current_message)
        

send_messages(messages[:])
print("Sent messages:")
print(sent_messages)
print(messages)