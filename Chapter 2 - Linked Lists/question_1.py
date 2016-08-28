from collections import Counter
from LinkedList import LinkedList

def remove_dupes(list):
  """ Removes all duplicate data"""
  n = list.head
  count = Counter()
  prev = list.head
  while n:
    count[n.data] += 1
    if count[n.data] > 1:
      if n == list.tail:
        list.tail = prev
      prev.next_node = n.next_node
    else:
      prev = n
    n = n.next_node
  return list


def remove_dupes2(list):
  """ Removes all duplicate data without outside data structures"""
  n = list.head
  if n:
    n2 = n.next_node
  while n:
    while n2:
      print(n.data, n2.data)
      n2 = n2.next_node
    n = n.next_node

my_list = LinkedList()
my_list.append_left('Rumm')
my_list.append_left('Rumm')
my_list.append_left('Rumm')
my_list.append_left('Rumm')
my_list.append_right('Rumm')
my_list = remove_dupes(my_list)
print(my_list)
