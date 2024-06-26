#!/usr/bin/env python3
"""Tasks"""

from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """task_wait_random"""
    return create_task(wait_random(max_delay))
