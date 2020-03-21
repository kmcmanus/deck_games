import string
import random

from functools import reduce

def add_random_letter_to(current, nxt):
  return current + random.choice(string.ascii_lowercase)

def random_token():
  return reduce(add_random_letter_to, xrange(4), '')

def generate_token(context=[]):
  token = random_token()
  tries = 100
  while token in context:
    tries -= 1
    if tries == 0:
      raise RuntimeError("Cannot generate token")
    token = random_token
  return token
