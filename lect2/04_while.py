def ask_user():
    while True:
        q = input("How are you? ")
        if q == "Fine":
            break


def chat():
    dialogue = {"zzz": "bye", "hello": "hi", "how are you?": "Good, thanks"}

    while True:
        try:
            prompt = input("Talk to bot: ").lower().strip()
            if prompt in dialogue.keys():
                print(dialogue[prompt])
                if prompt == 'zzz':
                    break
            else:  # add new phrase to dictionary
                answer = input("How should bot reply? ")
                dialogue[prompt] = answer
            print(f"This chat bot knows {len(dialogue)} phrases")
        except KeyboardInterrupt:
            print("See you soon!")
            break


ask_user()
chat()
