from collections import Counter

class LinkedList:
    class __Node:
        """ Node class represents an individual item in the list """
        def __init__(self, data, next_node):
            self.data = data
            self.next_node = next_node

        def __repr__(self):
            return str(self.data) + '=>'

    def __init__(self):
      self.head = None
      self.tail = None

    def append(self, data):
        """ Adds an item to the end (right side) of a list """
        node = self.__Node(data, None)
        if not self.head:
            self.head = node
        else:
            self.tail.next_node = node
        self.tail = node

    def append_left(self, data):
      """ Adds an item to the start(left side) of a list """
      node = self.__Node(data, None)
      node.next_node = self.head
      self.head = node

    def remove(self, data):
        """ Removes a node with the given data """
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                prev_node.next_node = current_node.next_node
                current_node = None
            else:
                prev_node = current_node
                current_node = current_node.next_node

    def remove_dupes(self):
      """ Removes all duplicate data"""
      n = self.head
      count = Counter()
      prev = self.head
      while n:
        count[n.data] += 1
        if count[n.data] > 1:
          prev.next_node = n.next_node
        prev = n
        n = n.next_node


    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node)
            current_node = current_node.next_node
        return ''.join(str(result))


my_list = LinkedList()
my_list.append('Lemmons')
my_list.append('Pie')
my_list.append('Rumm')

# Check the list
print(my_list)

# Remove the tails
my_list.remove('Rumm')
print(my_list)


my_list.append_left('Rumm')
print(my_list)

my_list.append_left('Rumm')
print(my_list)

my_list.remove_dupes()
print(my_list)
