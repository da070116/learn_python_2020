def ask_user():
    while True:
        q = input("How are you? ")
        if q == "Fine":
            break


def chat():
    dialogue = {"zzz": "bye", "hello": "hi", "how are you?": "Good, thanks"}
    while True:
        q = input("Talk to me! ").lower().strip()
        if q in dialogue.keys():
            print(dialogue[q])
            if q == 'zzz':
                break


chat()
