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
  while n:
    if n:
      n2 = n.next_node
      prev2 = n
      while n2:
        if n.data == n2.data:
          prev2.next_node = n2.next_node
        else:
          prev = n2
        n2 = n2.next_node
    n = n.next_node
  return list

my_list = LinkedList()
my_list.append_left('Rumm1')
my_list.append_left('Rumm2')
my_list.append_left('Rumm3')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
my_list.append_left('Rumm4')
print(my_list)
my_list = remove_dupes2(my_list)
print(my_list)
