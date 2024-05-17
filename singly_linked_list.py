class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return(f'Node | {self.value}')
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node


    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:   
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, value_to_remove):
        if self.head is None:
            print('This list is empty')
        if self.head.value == value_to_remove:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value_to_remove:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print(f'{value_to_remove} does not exist in this list.')

    def traverse(self):
        print('\nHere are your current list items: \n')
        current_node = self.head
        while current_node:
            print(current_node, end=' - > ')
            current_node = current_node.next
        print('\n\nList Complete!')

        
nodes = SinglyLinkedList()
nodes.push('chris')
nodes.push('ayden')
nodes.push('savvy')

nodes.append('jason')
nodes.append('clive')
nodes.append('karen')

nodes.remove('jason')

nodes.traverse()

