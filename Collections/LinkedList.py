class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print(self):
    nextNode = self.head
    while nextNode is not None:
      print(nextNode.value)
      nextNode = nextNode.next


myList = LinkedList()
myList.head = Node(1)
node2 = Node(2)
node3 = Node(3)

myList.head.next = node2
node2.next = node3

myList.print()