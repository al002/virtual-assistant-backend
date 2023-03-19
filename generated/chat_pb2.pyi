from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ["input"]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    input: str
    def __init__(self, input: _Optional[str] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ["error", "reply"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    error: str
    reply: str
    def __init__(self, reply: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class CodeGenerationChatRequest(_message.Message):
    __slots__ = ["position", "query", "tech_stacks"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TECH_STACKS_FIELD_NUMBER: _ClassVar[int]
    position: str
    query: str
    tech_stacks: str
    def __init__(self, position: _Optional[str] = ..., tech_stacks: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class TranslatorChatRequest(_message.Message):
    __slots__ = ["language", "query"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    language: str
    query: str
    def __init__(self, language: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...
