import math
import io_operations as io

class Statistics:
  def __init__(self):
    self.dictionary = {}

  def __init__(self, dict):
    self.dictionary = dict

  def add(self, key, value):
    if key in self.dictionary:
      self.dictionary[key] += round(value)
    else:
      self.dictionary[key] = round(value)

  def delete(self, key):
    if key in self.dictionary:
      del self.dictionary[key]
  
  def print(self):
    sum = 0
    for entry in self.dictionary:
      time = self.dictionary[entry]
      sum += time
      if time < 3600:
        minutes = time // 60
        seconds = time % 60
        print(f"{entry}: {round(minutes)} m, {seconds} s")
      else:
        minutes = ( time // 60 ) % 60
        hours = time // 3600
        print(f"{entry}: {math.floor(hours)} h, {round(minutes)} m")
    if sum < 3600:
      minutes = sum // 60
      seconds = sum % 60
      print(f"Sum: {round(minutes)} m, {seconds} s")
    else:
      minutes = ( sum // 60 ) % 60
      hours = sum // 3600
      print(f"Sum: {math.floor(hours)} h, {round(minutes)} m")

  def parse(self):
    res = ''
    for entry in self.dictionary:
      time = self.dictionary[entry]
      res+=entry+","+str(time)+"\n"
    return res

  def save(self):
    sorted_dict = dict(sorted(self.dictionary.items(), key=lambda x: x[0]))
    self.dictionary = sorted_dict
    io.save_statistics(self.parse())