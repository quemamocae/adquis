class RangeObj:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration
        current_value = self.current
        self.current += self.step
        return current_value

    def __repr__(self):
        return f"RangeObj({self.start}, {self.end}, {self.step})"

    def __len__(self):
        return max(0, (self.end - self.start + self.step - 1) // self.step)

    def __contains__(self, item):
        if self.step > 0:
            return self.start <= item < self.end and (item - self.start) % self.step == 0
        else:
            return self.start >= item > self.end and (self.start - item) % self.step == 0

# Example usage
range_obj = RangeObj(0, 10, 2)
print(range_obj)  # Output: RangeObj(0, 10, 2)

for num in range_obj:
    print(num)  # Output: 0, 2, 4, 6, 8

print(len(range_obj))  # Output: 5
print(4 in range_obj)  # Output: True
print(5 in range_obj)  # Output: False
