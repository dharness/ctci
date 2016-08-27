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

    def append(self, data):
        """ Adds an item to the end (right side) of a list """
        node = self.__Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next_node = node
        self.tail = node

    def append_left(self, data):
      """ Adds an item to the start(left side) of a list """
      node = self.__Node(data)
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

def test(list):

  # Remove the tails
  list.remove('Rumm')
  print(list)


  list.append_left('Rumm')
  print(list)

  list.append_left('Rumm')
  print(list)
