import struct
a = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM"
b = struct.pack("I", 0xcafebabe)
print a+b

