class LinkedListError(Exception):
    
    pass

class EmptyListError(LinkedListError):
   
    pass

class InvalidIndexError(LinkedListError):
    
    pass


class Node:
    
    def __init__(self, value):
        self.value = value      
        self.next_node = None  

    def __repr__(self):
       
        return f"Node({self.value})"


# The LinkedList Class


class LinkedList:
    
    def __init__(self):
        
        self.head = None       
        self.node_count = 0     

    def add_to_end(self, value):
       
        new_node = Node(value)
        print(f"Adding '{value}' to the end of our chain...")

        
        if self.head is None:
            self.head = new_node
        else:
           
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            
            
            current_node.next_node = new_node

        self.node_count += 1
    def display_chain(self):
        
        if self.head is None:
            print("The list is currently empty.")
            return

        print("Displaying the list:")
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(f"[ {current_node.value} ]")
            current_node = current_node.next_node
        
        print(" --> ".join(elements) + " --> END")
        print(f"(Total nodes: {self.node_count})")

    def remove_node_at(self, position):
        
        print(f"\nAttempting to remove node at position {position}...")

       
        if self.head is None:
            raise EmptyListError("Cannot delete from an empty list.")
        
        if not (1 <= position <= self.node_count):
            raise InvalidIndexError(f"Index {position} is out of range. "
                                    f"Valid positions are from 1 to {self.node_count}.")

       
        if position == 1:
            node_to_remove = self.head
            self.head = self.head.next_node
            print(f"Successfully removed '{node_to_remove.value}' from the head.")
        else:
           
            previous_node = self.head
            current_position = 1
            while current_position < position - 1:
                previous_node = previous_node.next_node
                current_position += 1
           
            node_to_remove = previous_node.next_node
            
           
            previous_node.next_node = node_to_remove.next_node
            print(f"Successfully removed '{node_to_remove.value}' at position {position}.")
        
        self.node_count -= 1



if __name__ == "__main__":
    print("--- EXAMPLE RUN ---")
    
    
    my_book_list = LinkedList()
    my_book_list.display_chain()

    
    print("\n--- Populating the list ---")
    my_book_list.add_to_end("The Hobbit")
    my_book_list.add_to_end("Dune")
    my_book_list.add_to_end("1984")
    my_book_list.add_to_end("Brave New World")
    print("\n--- List after adding nodes ---")
    my_book_list.display_chain()

   
    try:
        my_book_list.remove_node_at(3) 
        my_book_list.display_chain()
    except LinkedListError as e:
        print(f"Error: {e}")

    
    try:
        my_book_list.remove_node_at(1)
        my_book_list.display_chain()
    except LinkedListError as e:
        print(f"Error: {e}")

  
    try:
        my_book_list.remove_node_at(2) 
        my_book_list.display_chain()
    except LinkedListError as e:
        print(f"Error: {e}")

 
    try:
        
        my_book_list.remove_node_at(5)
    except InvalidIndexError as e:
        print(f"Caught expected error: {e}")
        my_book_list.display_chain()
        
   
    try:
        
        my_book_list.remove_node_at(1) 
        my_book_list.display_chain()
       
        my_book_list.remove_node_at(1)
    except EmptyListError as e:
        print(f"Caught expected error: {e}")

