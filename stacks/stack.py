# stacks are especially easily implemented in python
# since the list data structure already has very similar
# operations

class Stack(object):
    def __init__(self, list:list = []):
        self.list = list 

    # to define a push operation we simply utilize the append
    # function from list
    def push(self, value:any):
        self.list.append(value)

    # just as simply for the pop operation we can use list's
    # pop function
    def pop(self):
        try:
            self.list.pop()
        except:
            print("Given stack does not have any values to pop.")

    # create simple print helper function
    # otherwise using print would just show the object and their
    # hashcodes
    def printStack(self):
        print(self.list)

# some sample code to check the implementation so far
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.printStack()
# stack.pop()
# stack.printStack()
# stack.pop()
# stack.pop()s