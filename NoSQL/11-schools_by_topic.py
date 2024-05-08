#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic"""
    return [i for i in mongo_collection.find({"topics": topic})]