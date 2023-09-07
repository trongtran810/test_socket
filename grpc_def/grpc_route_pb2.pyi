from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Point(_message.Message):
    __slots__ = ["maths", "titerature"]
    MATHS_FIELD_NUMBER: _ClassVar[int]
    TITERATURE_FIELD_NUMBER: _ClassVar[int]
    maths: int
    titerature: int
    def __init__(self, maths: _Optional[int] = ..., titerature: _Optional[int] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ["categoryType"]
    CATEGORYTYPE_FIELD_NUMBER: _ClassVar[int]
    categoryType: str
    def __init__(self, categoryType: _Optional[str] = ...) -> None: ...
