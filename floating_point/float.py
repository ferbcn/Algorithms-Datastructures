a_str = '00000101'
b_str = '00000001'

class Binary:
    bin_int = 0

    def __init__(self, bin_str):
        self.bin_int = int(bin_str, 2)

    def sum(self, other_bin):
        return bin(self.bin_int + other_bin.bin_int)[2:]

    def sub(self, other_bin):
        return bin(self.bin_int - other_bin.bin_int)[2:]

    def mul(self, other_bin):
        return bin(self.bin_int * other_bin.bin_int)[2:]

    def div(self, other_bin):
        return bin(self.bin_int / other_bin.bin_int)[2:]

    def band(self, other_bin):
        return bin(self.bin_int & other_bin.bin_int)[2:]

    def bor(self, other_bin):
        return bin(self.bin_int | other_bin.bin_int)[2:]

    def bxor(self, other_bin):
        return bin(self.bin_int ^ other_bin.bin_int)[2:]



a = Binary(a_str)
b = Binary(b_str)

# print binary string
print(a.sum(b))
print(a.sub(b))
print(a.mul(b))
#print(a.div(b))
print(a.band(b))
print(a.bor(b))
print(a.bxor(b))
