'''
Node Class
'''
class Node:
	
	# ctor
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val

	# get the left node
	def getLeft(self):
		return self.left

	# get the right node
	def getRight(self):
		return self.right

	# get the data
	def getData(self):
		return self.data

	# print the node data
	def printData(self):
		print "",self.data,""


'''
BST Class
'''
class BST:

	# ctor
	def __init__(self):
		self.root = None

	# get the root of the tree
	def getRoot(self):
		return self.root

	# check whether 

	# helper recursive function to insert node
	def _insertNode(self, node, root):
		if root == None:
			root = node
		elif node.getData() <= root.getData():
			self._insertNode(node, root.getLeft())
		else:
			self._insertNode(node, root.getRight())

	# insert a node with given value into BST
	def insertNode(self, val):
		node = Node(val)
		self._insertNode(node, self.root)


if __name__ == "__main__":
	print "Here is the Tree:"
	bst = BST()
	bst.insertNode(4)
	print bst.getRoot()