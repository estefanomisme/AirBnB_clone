#!/usr/bin/python3
"""Class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city of a state"""
    state_id = ""
    name = ""
