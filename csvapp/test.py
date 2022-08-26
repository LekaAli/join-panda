def print_message(name, age):
    if age <= 18:
        msg = "you are still a teenager"
    elif 18 < age < 30:
        msg = "soon you need to start being responsible"
    else:
        msg = "you are now responsile"

    return name + ", " + msg


if __name__ == "__main__":
    name = X
    age = Y

    message = print_message(name, age)
    print(message)