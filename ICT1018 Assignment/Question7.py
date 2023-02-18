class Node: #node class defining the features of a node
    def __init__(self, val=None): #constructor identified by key word "__init__"
        self.left = None #left subtree is initialised to none
        self.right = None #right subtree is initialised to none
        self.val = val #the data part of the node which is initialised to none if no data is passed

    #method used to insert new nodes into the binary search tree
    def insert(self, value):
        #if the node does not have a value in it, i.e. it is empty, it is changed to 'value'
        if self.val is None: 
            self.val = value #placing the value in the node
            return #exiting the method

        #if the selected node contains the same value as the one entered by the user, a message is displayed
        if self.val == value:
            print ("Entered value already exists!") 
            return 

        #if the entered value is smaller than the selected value, place the value on the left side
        if value < self.val: 
            if self.left is not None: #if the first left child is occupied, recursviely call the method 
                self.left.insert(value)
                return
            #if the left child is empty, place the value in a new node on the left
            self.left = Node(value)  #creating a new node
            return

        #if the entered value is greater than the selected value place the value on the right side
        else:
            if self.right is not None: #if the first right child is occupied, recursviely call the method 
                self.right.insert(value)
                return
            #if the right child is empty, place the value in a new node on the right
            self.right = Node(value)
            return

    #algorithm used to print the BST in order
    def inorder(self, value):
        if self.left is not None: #checking if the node is empty
            self.left.inorder(value)
        if self.val is not None:
            print (self.val) #printing the value
        if self.right is not None:
            self.right.inorder(value)
        return value #if the node is empty, the value is printed

bst = Node() #creating the first Node
bst.insert(10)
bst.insert(20)
bst.insert(-1)
bst.insert(100)
bst.insert(-10)
bst.insert(10)

"""print("Press '0' if you want to stop entering numbers")
flag = 0
while flag != 1:
    a = int(input("Please enter a number!  ")) #number used for BST
    if a == 0:
        flag = 1
    else:
        bst.insert(a) #adding the number to the BST"""

print("Printing the BST inorder")
bst.inorder(None) #calling the inorder method