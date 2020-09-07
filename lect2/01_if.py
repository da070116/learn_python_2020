def define_activity(age: int) -> str:
    if 0 < age < 7:
        activity = "attend kindergarten or stay at home"
    elif 7 <= age < 18:
        activity = "study at school"
    elif 18 <= age < 23:
        activity = "study at university"
    elif age > 65:
        activity = "rest in retirement"
    else:
        activity = "work hard"
    return activity


if __name__ == '__main__':
    user_age = int(input("What is your age? "))
    print(f"You should {define_activity(user_age)} by the age of {user_age}")
