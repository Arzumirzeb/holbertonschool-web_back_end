#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""
    def multiply(a: float) -> float:
        """function for multiplying"""
        return a * multiplier
    return multiply
