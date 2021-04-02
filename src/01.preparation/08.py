import re

STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

def cipher(sent):
    decode_list = []
    for x in sent:
        if re.match("[a-z]", x):
            decode_list.append(chr(219 -ord(x)))
        else:
            decode_list.append(x)
    return "".join(decode_list)

decode = cipher(STR)
encode = cipher(decode)

print(decode)
print(encode)