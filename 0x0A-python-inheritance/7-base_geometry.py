#!/usr/bin/python3
"""
Module 5-base_geometry
Contains empty class BaseGeometry
"""
class BaseGeometry:
    """ public instance to raise excepton"""
    def area(self):
        "raise exception area() is not implemented"
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

