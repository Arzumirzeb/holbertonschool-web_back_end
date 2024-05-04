#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime function"""
    runtime = time()
    await gather(*[async_comprehension() for i in range(4)])
    return time() - runtime
