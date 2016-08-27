from collections import Counter
from LinkedList import my_list

def remove_dupes(list):
  """ Removes all duplicate data"""
  n = list.head
  count = Counter()
  prev = list.head
  while n:
    count[n.data] += 1
    if count[n.data] > 1:
      prev.next_node = n.next_node
    else:
      prev = n
    n = n.next_node
  return list

my_list.append('Rumm')
my_list.append('Rumm')
print(my_list)
my_list = remove_dupes(my_list)
print(my_list)
