#!/usr/bin/python -tt

import pytest
import sys
import time

from linkedlist import Node, LinkedList

def test_insert():
    l_list = LinkedList()
    l_list.insert("David")
    assert l_list.head.get_data() == "David"
    assert l_list.head.get_next() is None

def test_insert_two():
    l_list = LinkedList()
    l_list.insert("David")
    l_list.insert("Thomas")
    assert l_list.head.get_data() == "Thomas"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "David"

def test_nextNode():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    assert l_list.head.get_data() == "Rasmus"
    head_next = l_list.head.get_next()
    assert head_next.get_data() == "Pallymay"
    last = head_next.get_next()
    assert last.get_data() == "Jacob"

def test_positive_search():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    found = l_list.search("Pallymay")
    assert found.get_data() == "Pallymay"
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"

def test_searchNone():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    # make sure reg search works
    found = l_list.search("Jacob")
    assert found.get_data() == "Jacob"
    with pytest.raises(ValueError):
        l_list.search("Vincent")

def test_delete():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Rasmus")
    assert l_list.head.get_data() == "Pallymay"
    l_list.delete("Jacob")
    assert l_list.head.get_next() is None

def test_delete_value_not_in_list():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    with pytest.raises(ValueError):
        l_list.delete("Sunny")

def test_delete_empty_list():
    l_list = LinkedList()
    with pytest.raises(ValueError):
        l_list.delete("Sunny")

def test_delete_next_reassignment():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Cid")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.delete("Pallymay")
    l_list.delete("Cid")
    assert l_list.head.next_node.get_data() == "Jacob"  

def test_remove_duplicates():
    l_list = LinkedList()
    l_list.insert("Rasmus") 
    l_list.insert("Cid")
    l_list.insert("Cid")
    l_list.remove_duplicates_no_buffer()
    assert l_list.head.next_node.get_data() == "Rasmus"
    l_list.insert("Cid")
    l_list.remove_duplicates()
    assert l_list.head.next_node.get_data() == "Rasmus"
    
def test_corrupt_loop():
  l_list = LinkedList()
  l_list.insert('Jacoby')
  l_list.insert('Jalen')
  l_list.insert('Jacoby')
  l_list.insert('Bill')
  l_list.insert('Billy')
  node1 = l_list.search('Jacoby')
  node2 = l_list.search('Billy')
  node1.set_next(node2)
  node = l_list.corrupt_loop()
  assert node.get_data() == "Billy"

def find_nth_to_last_recursive(head,n):
  if head == None:
    return 0
  i = find_nth_to_last_recursive(head.get_next(),n) + 1
  if i == n:
    print head
  return i

def remove_

def main():
  test_insert()
  test_insert_two()
  test_nextNode()
  test_positive_search()
  test_searchNone()
  test_delete()
  test_delete_value_not_in_list()
  test_delete_empty_list()
  test_delete_next_reassignment()
  test_remove_duplicates()
  test_corrupt_loop()

  l_list = LinkedList()
  l_list.insert('Jacoby')
  l_list.insert('Jalen')
  l_list.insert('Jacobian')
  l_list.insert('Bill')
  l_list.insert('Billy')
  node = l_list.find_nth_to_last(4)
  print node.get_data()
  find_nth_to_last_recursive(l_list.head,6)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
