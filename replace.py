binary = "101"


def replace(bin):
    out = ""
    bin = [int(i) for i in list(bin)]
    for i in bin:
        out += "1" if i == 0 else "0"
    return "".join(out)


print(replace(binary))
