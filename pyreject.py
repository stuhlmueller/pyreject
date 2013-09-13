#!/usr/bin/env python

from __future__ import division
from math import log
from collections import defaultdict

class ConditionViolated(Exception):
  pass

def query(proc):
  def new_proc():
    while True:
      try:
        val = proc()
      except ConditionViolated:
        continue
      else:
        return val
  return new_proc

def observe(x):
  if not x:
    raise ConditionViolated

def normalize(counts):
  Z = sum(counts.values())
  return dict((k, c/Z) for (k, c) in counts.items())    

def dist(model, n):
  counts = defaultdict(lambda: 0)
  for _ in xrange(n):
    sample = model()
    counts[sample] += 1
  return normalize(counts)    

def expectation(model, f, n):
  expected_value = 0.0
  for (val, prob) in dist(model, n=n).items():
    expected_value += prob * f(val, prob)
  return expected_value

def surprisal(prob):
  return -log(prob, 2)

def entropy(model, n):
  return expectation(model, lambda val, prob: surprisal(prob), n=n)
    
