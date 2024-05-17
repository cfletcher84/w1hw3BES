class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return(f'Player: {self.name} Scored: {self.score}')
    
class Node:
    def __init__(self, player):
        self.player = player
        self.next = None
        self.prev = None
    
class DoubleyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_player(self, name, score):
        new_player = Player(name, score)
        new_node = Node(new_player)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        print(f'{new_node.player} added to the front of the doubly linked list.')


    def remove_player(self, name):
        if self.head is None:
            print('Empty List')
            return
        if self.head.player.name == name:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.player.name == name:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
            print(f'{name} was remnoved from the list!')
            return
        
    def traverse(self):
        print('Here are your players and their score.')
        current = self.head
        while current:
            print(current.player, end=" | ")
            current = current.next
        print('\nThe list has ended.')


play = DoubleyLinkedList()
play.add_player('chris', 100)
play.add_player('ayden', 200)
play.add_player('clive', 300)
play.remove_player('chris')
play.traverse()