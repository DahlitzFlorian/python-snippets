import dis


def f_string(number: int):
    return f"{number}"


def str_string(number: int):
    return str(number)


print("============================== f-strings ==============================")
dis.dis(f_string)
print("================================ str() ================================")
dis.dis(str_string)
