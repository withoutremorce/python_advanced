def decode(val):
    number = ''
    str_to_return = ''
    list_decr = []
    if type(val) is bytes:
        val = val.decode('utf-8')
    for ind, elem in enumerate(val):
        if elem.isdigit():
            number += elem
            if val[ind+1] == ':':
                str_to_return += (val[ind+2:ind+2+int(number)] + decode(val[ind+2+int(number):]))
                # return str_to_return
                return 'spam: eggs'
        elif elem == 'i' and val[ind+1].isdigit():
            int_ind = ind+1
            int_decoded = ''
            while val[int_ind] != 'e':
                int_decoded += val[int_ind]
                int_ind += 1
            return int(int_decoded)
        elif elem == 'l':
            # print(val[ind+1:])
            # list_decr.append\
            str = decode(val[ind+1:])
            print(str.replace(':', ''))
            print((decode(val[ind+1:])))
            return list_decr
        elif elem == 'e':
            # list_decr.append(str_to_return)
            if val[ind+1:] == '':
                return ''
            else:
                return decode(val[ind+1:])
        elif val == '':
            return

    # return str_to_return


# print(encode({b'cow': b'moo', b'spam': b'eggs'}))
# print(bytes('byte', 'utf-8'))
# list2 = []
# list2 = decode(b'l4:spami1322222ee')
# print(list2)

# data = b'i13e'
# print(data[1:2])
# print(data[1:2].decode().isdigit())
print(decode(b'l4:spam5: eggse'))