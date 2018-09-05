import pytest

@pytest.mark.parametrize('a, b', [
    ('spam',bytes('4:spam')),
    ('', bytes('0:')),
    # 'вффывфв'
])
def test_encode_str(a,b):
    pass

@pytest.mark.parametrize('a, b', [
    (bytes('spam'),bytes('4:spam'))
])
def test_encode_bytes(a,b):
    pass

@pytest.parametrize('a, b', [
    (3, bytes('i3e')),
    (-3, 'i-3e'),
    (0, 'i0e'),
])
def test_encode_int(a,b):
    bytes(b) == encode(a)
    # with pytest.raises(Exception):
    #     'i03e'

def test_encode_list(a,b):
    pass
def test_encode_dict(a,b):
    pass

def test_decode_int(a,b):
    with pytest.raises(Exception):
        'i03e'