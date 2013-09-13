# PyReject

A tiny library for writing probabilistic models with rejection query inference in Python.

## Usage example

Model:

    import random

    from pyreject import *

    def flip(p):
      return random.random() < p

    @query
    def foo():
      x = flip(.5)
      y = flip(.5)
      observe(x or y)
      return x, y

Estimating distributions:

    >>> dist(foo, n=10000)

    {(False, True): 0.3345, (True, False): 0.3313, (True, True): 0.3342}

Expectations:

    def f(value, prob):
      x, y = value
      return 1 if x or y else 0

    >>> expectation(foo, f, n=10000)

    1.0

Entropy:

    >>> entropy(foo, n=10000)

    1.58455505656
