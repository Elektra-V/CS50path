"""dum de dum de dum de dum
    enters cookie monster"""

class Jar:
    # initialising the object with some default values
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    # string method to print desired output
    def __str__(self):
        return "🍪" * self.size
    
    # if jar has capacity add cookies to it 
    def deposit(self, n):
        if n > (self.capacity - self.size):
            raise ValueError("Cookies overflow")
        self.size += n 

    # when hungry take out those cookies 
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self.size -= n

    # getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0 :
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    # getter for size
    @property
    def size(self):
        return self._size

    # setter for size
    @size.setter
    def size(self, size):
        if int(size) < 0:
            raise ValueError("Size cannot be negative")
        self._size = size

 
def main():
    """ gobble gobble """
    jar = Jar(20)
    jar.deposit(13)
    jar.withdraw(5)
    print(jar.capacity)
    print(jar.size)
    print(jar)


if __name__ == "__main__":
    main()