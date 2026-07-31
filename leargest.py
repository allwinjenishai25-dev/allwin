class largest():
    def __init__(self):
        self.largest=None

    def find_largest(self,numbers):
        if not numbers:
            return None

        self.largest=numbers[0]

        for number in numbers:
            if number > self.largest:
                self.largest=number
        return self.largest
numbers=[int(x) for x in input("Enter number separated by space:").split()]
obj = largest()
print("The largest number is :", obj.find_largest(numbers))