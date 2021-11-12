#!/usr/bin/python3
"""Class state"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a state of a country"""
    place_id = ""
    user_id = ""
    text = ""
