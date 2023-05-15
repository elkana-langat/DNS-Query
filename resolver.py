from dataclasses import dataclass
import dataclasses
import struct

@dataclass
class DNSHeader:
    id: int
    flags: int
    num_questions : int = 0
    num_answers: int = 0
    num_authorities: int = 0
    num_additionals: int = 0

@dataclass
class DNSQuestion:
    name: bytes
    type_: int
    class_: int

# Convert python classes to string bytes
def header_to_bytes(header):
    fields = dataclass.astuple(header)
    # there are 6 `H`s because there are 6 fields
    return struct.pack("!HHHHHH", *fields)

def question_to_bytes(question):
    return question.name + struct.pack("!HH", question.type_, question.class_)

