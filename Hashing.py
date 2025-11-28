
class HashFunctions:
    def __init__(self, table_size):
        self.size = table_size

    def division_method(self, key):
        return key % self.size

    def multiplication_method(self, key):
        A = 0.6180339887  # constant fractional part of golden ratio
        frac = (key * A) % 1
        return int(self.size * frac)

    def mid_square_method(self, key):
        sq = key * key
        sq_str = str(sq)
        mid = len(sq_str) // 2
        # take 2 middle digits or less if short number
        if len(sq_str) < 2:
            mid_digits = sq_str
        else:
            mid_digits = sq_str[max(0, mid-1):mid+1]
        return int(mid_digits) % self.size

    def folding_method(self, key):
        s = str(key)
        total = 0
        # add parts of 2 digits each
        for i in range(0, len(s), 2):
            part = s[i:i+2]
            total += int(part)
        return total % self.size

# Example usage with multiple keys:
hf = HashFunctions(10)
keys = list(map(int, input("Enter Keys separated by spaces:").split()))

print("Key    Division   Multiplication   Mid Square   Folding")
for key in keys:
    d = hf.division_method(key)
    m = hf.multiplication_method(key)
    ms = hf.mid_square_method(key)
    f = hf.folding_method(key)
    print(f"{key}   {d:^8}   {m:^14}   {ms:^10}   {f:^7}")
