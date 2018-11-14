import hashlib as hashlib
import datetime as date

class Block:
  def __init__(self, index, data, previous_hash):
    self.index = index
    self.timestamp = date.datetime.now()
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hashlib.sha256()
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
    return sha.hexdigest()

  def __str__(self):
    return 'Index: ' + str(self.index) + \
      '\nCreated: ' + str(self.timestamp) + \
      '\nData: ' + str(self.data) + \
      '\nHash: ' + str(self.hash) + '\n'

class Chain(list):
  def __delitem__(self, index):
    raise NotImplementedError

  def __delslice__(self, index):
    raise NotImplementedError

  def __setitem__(self, index):
    raise NotImplementedError

  def __setslice__(self, index):
    raise NotImplementedError

  def insert(self):
    raise NotImplementedError

  def pop(self):
    raise NotImplementedError

  def remove(self):
    raise NotImplementedError

  def __str__(self):
    return "".join(str(block) for block in self)


blockchain = Chain()
blockchain.append(Block(0, "Genesis Block", "0"))

new_block=Block(len(blockchain), "More data", blockchain[:1][0].hash)
blockchain.append(new_block)

print str(blockchain)

# del blockchain[0]
