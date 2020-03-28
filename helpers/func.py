from copy import copy

def depy(func):
  def anon(item):
    clone = copy(item)
    func(clone)
    return clone
  return anon
