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
from django.conf import settings
import re
import string
import itertools as it

if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
    )


def encode(val):
    if isinstance(val, int):
        return b"i" + str(val).encode() + b"e"
    elif isinstance(val, bytes):
        return str(len(val)).encode() + b":" + val
    elif isinstance(val, str):
        return encode(val.encode("utf-8"))
    elif isinstance(val, list):
        return b"l" + b"".join(map(encode, val)) + b"e"
    elif isinstance(val, dict):
        if all(isinstance(i, bytes) for i in val.keys()):
            items = list(val.items())
            items.sort()
            return b"d" + b"".join(map(encode, it.chain(*items))) + b"e"
        else:
            raise ValueError("dict keys should be bytes")
    raise ValueError("Allowed types: int, bytes, list, dict; not %s", type(val))


def decode(s):
    def decode_first(s):
        if s.startswith(b"i"):
            match = re.match(b"i(-?\\d+)e", s)
            return int(match.group(1)), s[match.span()[1]:]
        elif s.startswith(b"l") or s.startswith(b"d"):
            lst = []
            slice = s[1:]

            while not slice.startswith(b"e"):
                elem, slice = decode_first(slice)
                lst.append(elem)
            slice = slice[1:]
            if s.startswith(b"l"):
                return lst, slice
            else:
                return {i: j for i, j in zip(lst[::2], lst[1::2])}, slice
        elif any(s.startswith(i.encode()) for i in string.digits):
            m = re.match(b"(\\d+):", s)
            length = int(m.group(1))
            slice_i = m.span()[1]
            start = slice_i
            end = slice_i + length
            return s[start:end], s[end:]
        else:
            raise ValueError("Malformed input.")

    if isinstance(s, str):
        s = s.encode("utf-8")

    ret, slice = decode_first(s)
    if slice:
        raise ValueError("Malformed input.")
    return ret