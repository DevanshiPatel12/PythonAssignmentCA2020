# Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]

class number:
    list1 = []
    list2 = []
    def __init__(self, array):
        self.array = array
    def find(self):
        for i in range(0, len(self.array) - 2):
            for j in range(i+1, len(self.array) - 1):
                for k in range(j+1, len(self.array)):
                    if self.array[i] + self.array[j] + self.array[k] == 0:
                        self.list1.append(self.array[i])
                        self.list1.append(self.array[j])
                        self.list1.append(self.array[k])
                        self.list2.append(self.list1)
                        self.list1 = []
        print("New list : ", self.list2)

n = number([-25,-10,-7,-3,2,4,8,10])
n.find()