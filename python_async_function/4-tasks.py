#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait-random function"""
    wait = []
    for i in range(n):
        wait.append(await task_wait_random(max_delay))
    return sorted(wait)
