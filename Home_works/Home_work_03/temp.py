# bencoding
# http://www.bittorrent.org/beps/bep_0003.html

# Strings are length-prefixed base ten followed by a colon and the string.
# For example 4:spam corresponds to 'spam'.

# Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
# For example i3e corresponds to 3 and i-3e corresponds to -3.
# Integers have no size limitation. i-0e is invalid.
# All encodings with a leading zero, such as i03e, are invalid,
# other than i0e, which of course corresponds to 0.

# Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
# For example l4:spam4:eggse corresponds to ['spam', 'eggs'].

# Dictionaries are encoded as a 'd' followed by a list of alternating keys
# and their corresponding values followed by an 'e'.
# For example, d3:cow3:moo4:spam4:eggse corresponds to {'cow': 'moo', 'spam': 'eggs'}
# Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).


def enc_list_dict(seq):
    temp_list = list()
    temp_string = b''
    if type(seq) is list:
        for elem in seq:
            if type(elem) is list or type(elem) is tuple or type(elem) is dict:
                # print('inserted list')
                temp_list.append(encode(elem))
            else:
                temp_list.append(encode(elem))
    # print('temp_list {}'.format(temp_list))
    if type(seq) is dict:
        for key, value in seq.items():
            if type(value) is list or type(value) is tuple or type(value) is dict:
                # print('inserted list')
                temp_list.append(encode(value))
            else:
                temp_list.append(encode(key))
                temp_list.append(encode(value))
    for temp_elem in temp_list:
        temp_string += temp_elem
    return temp_string


def decr_list(seq):
    list = []
    data = seq[1:-1]
    for ind, elem in enumerate(data.decode()):
        if elem.isdigit() and data[ind+1:ind+2] == b':':
            str_to_decode = decode(data[ind:data[ind]])
            list.append(str_to_decode)
        elif elem == 'i' and data[ind+1:ind+2].decode().isdigit():
            for int_ind, look_for_int in enumerate(data[ind:].decode()):
                if look_for_int == 'e':
                    e = int_ind + ind
                    break
            list.append(data.decode()[ind+1:e])
        # elif elem == 'l' and data[ind+1:ind+2] !=
    return list

def encode(val):
    if type(val) is bytes:
        # print('str {}'.format(enc_str(val)))
        val =  bytes(str(val.__len__()), 'utf-8')+b':'+val
        return val

    elif type(val) is int:
        # print('i'+str(val)+'e')
        return bytes('i'+str(val)+'e', 'utf-8')

    elif type(val) is list:
        return b'l'+enc_list_dict(val)+b'e'

    elif type(val) is dict:
        return b'd'+enc_list_dict(val)+b'e'
    else:
        print('not valid type')


def decode(val):
    if val.decode()[0].isdigit():
        # first, second = val.split(':')
        #
        # # print(first+' '+second)
        # # print(second[:int(first)])
        # return second[:int(first)]
        delim_pos = val.index(ord(':'))
        length = val[0:delim_pos]
        length = int(length)
        delim_pos += 1
        bstring = val[delim_pos:delim_pos + length]
        if len(bstring) != length:
            raise ValueError("Incorrect bencoded string length")
        return bstring
    elif val.startswith(b'i') and val.endswith(b'e'):
        # print(val[1:-1])
        end_pos = val.index(ord('e'))
        num_str = val[1:end_pos]
        return int(num_str)
    elif val.startswith(b'l') and val.endswith(b'e'):
        return decr_list(val)
    elif val.startswith(b'd') and val.endswith(b'e'):
        print('here4')
    else:
        print('not valid format for decrypt')


# print(encode({b'cow': b'moo', b'spam': b'eggs'}))
# print(bytes('byte', 'utf-8'))
list2 = []
list2 = decode(b'l4:spami1322222ee')
print(list2)

# data = b'i13e'
# print(data[1:2])
# print(data[1:2].decode().isdigit())