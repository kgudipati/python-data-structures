'''
Node Class
'''
class Node:
	
	# ctor
	def __init__(self, val):
		self.next = None
		self.data = val

	# get the next node
	def getNext(self):
		return self.next

	# get the data
	def getData(self):
		return self.data

	# print the node data
	def printData(self):
		print "",self.data,""


class LinkedList:

	# ctor
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	# insert a node to the front of LL
	def insertFront(self, val):
		node = Node(val)

		if self.head == None:
			self.head = node
			self.tail = node
		else:
			tmp = self.head
			self.head = node
			node.next = tmp
		self.size += 1

	# insert a node to the back of LL
	def insertBack(self, val):
		node = Node(val)

		if self.tail == None:
			self.head = node
			self.tail = node
		else:
			tmp = self.tail
			tmp.next = node
			self.tail = node
		self.size += 1

	# remove a node from the front of LL
	def removeFront(self):
		if self.head == None:
			print "LL is empty! Cannot remove from front."
			return
		else:
			tmp = self.head.next
			del self.head
			self.head = tmp
			self.size -= 1

	# remove a node from the back of LL
	def removeBack(self):
		if self.tail == None:
			print "LL is empty! Cannot remove from back."
			return
		
		# traverse list to second to last node
		ptr = self.head
		
		while ptr.next.next != None:
			ptr = ptr.next

		del self.tail
		self.tail = ptr
		self.tail.next = None
		self.size -= 1

	# print first node in Linked List
	def printFirst(self):
		print self.head.data

	# print last node in Linked List
	def printLast(self):
		print self.tail.data

	# print out the LL
	def printLL(self):
		ptr = self.head
		while ptr != None:
			print (ptr.data)
			ptr = ptr.next
		print "LL is size: ",self.size


if __name__ == "__main__":
	ll = LinkedList()
	ll.insertFront(3)
	ll.insertFront(4)
	ll.insertBack(2)
	ll.printFirst()
	ll.printLast()
	#ll.removeFront()
	#ll.removeBack()
	print "The List:"
	ll.printLL()