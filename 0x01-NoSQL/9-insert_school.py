#!/usr/bin/python3
"""Module for 9-insert_school.py"""



def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
