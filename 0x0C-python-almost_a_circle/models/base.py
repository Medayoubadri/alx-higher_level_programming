#!/usr/bin/python3
"""
This module provides the Base class for other models to inherit from.
"""
import json
import csv
import turtle


class Base:
    """
    The Base class from which other classes will inherit.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The id for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (dict):
                A double pointer to a dictionary of attributes.

        Returns:
            Base: An instance of a class that inherits from Base.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.

        Returns:
            list: A list of instances based on the class (cls).
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to a CSV file.

        Args:
            list_objs (list): List of instances inheriting from Base.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                        ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                        ])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.

        Returns:
            list: A list of instances of cls.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                objs = []
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                        objs.append(cls.create(**obj_dict))
                elif cls.__name__ == "Square":
                    for row in reader:
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                        objs.append(cls.create(**obj_dict))
                return objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all
        the Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects to be drawn.
            list_squares (list): List of Square objects to be drawn.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        pen.hideturtle()
        screen.exitonclick()