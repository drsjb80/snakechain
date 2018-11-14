import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
    return sha.hexdigest()

  def __str__(self):
    return 'Index: ' + str(self.index) + \
      '\nCreated: ' + str(self.timestamp) + \
      '\nData: ' + str(self.data)

import datetime as date

def create_genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block, data):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = data
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)
