from mailtm import Email

def main():
    email = Email()
    email.register()
    print("\nemail address: " + str(email.address))

    email.start(listener, interval=8)
    print("\nlistening for new emails...")

def listener(message):
    print(f"\nfrom: {message['from']['address']}")
    print(f"subject: {message['subject']}")
    print(f"body: {message['text']}")

if __name__ == '__main__':
    main()
