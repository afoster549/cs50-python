class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError

        self.cookies = 0

    def __str__(self):
        return f"{'🍪' * self.cookies}"

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.cookies - n >= 0:
            self.cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
