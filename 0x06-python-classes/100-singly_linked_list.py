#!/usr/bin/python3
"""
Module that defines a `Node` class for a singly linked list
and a `SinglyLinkedList` class to manage the linked list.
"""


class Node:
    """
    Class that defines a node for a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.
        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the list (default is None).
        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.
        Args:
            value (int): The data value for the node.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node.
        Args:
            value (Node): The next node in the linked list.
        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Defines the string representation of the linked list.
        Returns:
            A string containing all nodes' data, each on a new line.
        """
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.
        Args:
            value (int): The value to insert into the linked list.
        """
        new_node = Node(value)

        # If the list is empty or the new node should be the new head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse the list to find the correct position
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
