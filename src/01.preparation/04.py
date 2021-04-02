STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
GET_FIRST_ONE_WORD_LIST_INDEX = [1, 5, 6, 7, 8, 9, 15, 16, 19]

str_list = STR.split()

str_dict = {}
for i in range(len(str_list)):
    if i + 1 in GET_FIRST_ONE_WORD_LIST_INDEX:
        str_dict[i + 1] = str_list[i][0]
    else:
        str_dict[i + 1] = str_list[i][:2]

print(str_dict)

