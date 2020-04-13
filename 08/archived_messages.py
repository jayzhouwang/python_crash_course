def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop()
        print(msg)
        sent_messages.append(msg)


messages = ['I love you.', 'I hate you.', 'Here you are.']
sent_messages = []

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
