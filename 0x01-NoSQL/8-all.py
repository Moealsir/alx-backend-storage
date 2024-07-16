#!/usr/bin/python3
"""Module for 8-all.py"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    if not mongo_collection:
        return []
    return [item for item in mongo_collection.find()]
