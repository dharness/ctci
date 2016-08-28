from LinkedList import my_list

def remove_dupes(list):
  """ Removes all duplicate data"""
  n = list.head
  while n:
    print(n.data)
    n = list.next_node


print(my_list)
