#!/usr/bin/env python3
"""Module for 10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """Updates all documents in a collection based on name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
