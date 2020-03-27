import time

start_time = time.time()


class BStrTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.value:
            self.value = value
        else:
            if self.value > value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BStrTree(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BStrTree(value)

    def find(self, value):
        if self.value == value:
            return True

        elif self.value > value:
            if not self.left:
                return False
            else:
                return self.left.find(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.find(value)


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree = BStrTree()

# Time = O(nlog(n)) => about 0.1 seconds
for name_1 in names_1:
    tree.insert(name_1)
for name_2 in names_2:
    if tree.find(name_2):
        duplicates.append(name_2)

# Time = O(n^2) => about 11 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient
# approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions
# on techniques or data
# structures, but you may not import any additional libraries that you did not
# write yourself.
