import unittest

class LinkedList:
    class __Node:
        """ Node class represents an individual item in the list """
        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

        def __repr__(self):
            return str(self.data) + '=>'

    def __init__(self):
      self.head = None
      self.tail = None

    def append_right(self, data):
        """ Adds an item to the end (right side) of a list """
        node = self.__Node(data)
        n = self.head
        if n is None:
          self.head = node
          self.tail = node
        else:
          self.tail.next_node = node
          self.tail = node

    def append_left(self, data):
      """ Adds an item to the start(left side) of a list """
      node = self.__Node(data)
      node.next_node = self.head
      self.head = node
      if self.tail is None:
        self.tail = self.head

    def remove(self, data):
        """ Removes a node with the given data """
        current_node = self.head
        prev_node = None
        while current_node:
            # Found it
            if current_node.data == data:
                # TAIL
                if current_node == self.tail:
                    self.tail = prev_node
                    if current_node == self.head:
                        self.head = None
                if prev_node:
                  prev_node.next_node = current_node.next_node
                current_node = None
            else:
                prev_node = current_node
                current_node = current_node.next_node

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            if current_node == self.head:
                result.append('H')
            if current_node == self.tail:
                result.append('T')
            result.append(current_node)
            current_node = current_node.next_node
        return ''.join(str(result))

def test_append_right():
  print('Append Right ---')
  my_list = LinkedList()
  print(my_list)
  my_list.append_right('Rumm')
  print(my_list)

def test_remove():
  print('Remove ---')
  my_list = LinkedList()
  my_list.append_right('Rumm')
  print(my_list)
  my_list.remove('Rumm')
  print(my_list)
  my_list.append_right('Rumm')
  my_list.append_right('Rumm')
  my_list.append_right('Rumm')
  print(my_list)
  my_list.remove('Rumm')
  print(my_list)
  my_list.append_left('Rumm')
  print(my_list)
  my_list.remove('Rumm')
  my_list.remove('Rumm')
  my_list.remove('Rumm')
  my_list.remove('Rumm')
  my_list.remove('Rumm')
  print(my_list)

if __name__ is '__main__':
  test_append_right()
  test_remove()
