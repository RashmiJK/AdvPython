from typing import Union
from typing import overload

@overload
def bytes_getitem(b: bytes, idx: int) -> int:
    ...
@overload
def bytes_getitem(b: bytes, idx: slice) -> bytes:
    ...

def bytes_getitem(b: bytes, idx: Union[int, slice]) -> Union[int, bytes]:
    """
    if isinstance(idx, int):
        return
    else:
        return
    """
    return b[idx]

foo = b"1987$hello"
print(chr(bytes_getitem(foo, 0)))
print(bytes_getitem(foo, slice(5, 10)))
