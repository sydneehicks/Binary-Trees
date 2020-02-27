class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  
        self.right = None 


class BSTree:
    def __init__(self):
        self.root = None

    #BST insert
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data) 
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data) 

    #BST find
    def find(self,data):
        if not self.root:
            return False
        else:
            return self.findNode(data,self.root)

    def findNode(self,data,node):
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self.findNode(data,node.left)
        if data > node.data:
            return self.findNode(data,node.right)

    #BST traverse
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print(node.data)
        if node.right:
            self.traverseInOrder(node.right)

    #BST remove
    def remove(self,data):
        if self.root:
            self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(data,node.left)
        elif data > node.data:
            node.right = self.removeNode(data,node.right)
        else:
            #check no children case
            if not node.left and not node.right:
                print("removing a leaf node ...")
                del node
                return None

            #remove node with single child
            if not node.left:  #remove node with single right child
                print("removing a node with a single right child ...")
                tempnode = node.right
                del node
                return tempnode
            elif not node.right: #remove node with single ledt child
                print("removing a node with a single left child ...")
                tempnode = node.left
                del node
                return tempnode

            #remove node with two children
            print("removing a node with two children...")
            tempnode = self.getPredecessor(node.left)
            node.data = tempnode.data
            node.left = self.removeNode(tempnode.data, node.left)
        
        return node

    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

    #BST get min val
    def getMinVal(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.left:
            return self.getMin(node.left)

        return node.data
#==============================================================
"""
Assessment: 
Follow directions carefully:
   a. Instantiate a BST
   b. Insert 12 values into the tree using the 'insert' method
   c. Perform part b for two different orderings of the same 12 values you chose
   d. Traverse the tree to make sure the values you entered are contained in the tree
   e. Draw a picture of your tree for both orderings.
   f. Write a few sentences explaing how the insert method works (i.e. explain
      how a value is inserted into the tree, whatsteps a required to do so).

"""
bst = BSTree()
bst.insert(7)
bst.insert(6)
bst.insert(8)
bst.insert(5)
bst.insert(9)
bst.insert(4)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)

st = BSTree()
st.insert(3)
st.insert(4)
st.insert(5)
st.insert(7)
st.insert(8)
st.insert(9)
st.insert(6)
st.insert(1)
st.insert(2)
st.insert(12)
st.insert(11)
st.insert(10)

#The insert function takes the data given and makes it a node. Then it compares the new data to the node that was inserted before and determines if it goes the right or left of the node before.