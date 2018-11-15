import hashlib
import datetime
import unittest

# based on https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

def hash(block):
    sha256 = hashlib.sha256()
    sha256.update(str(block.index) + str(block.timestamp) + 
        str(block.data) + str(block.previous_hash))
    return sha256.hexdigest()

def verify(block, previous):
    block_hash = hash(block)
    return block.hash == block_hash and previous.hash == block.previous_hash

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash(self)

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

if "__main__" == __name__:
    blockchain = Chain()
    genesis_block = Block(0, "Genesis Block", "0")
    blockchain.append(genesis_block)

    new_block=Block(len(blockchain), "More data", blockchain[-1:][0].hash)
    blockchain.append(new_block)

    print str(blockchain)

class TestSnakeChain(unittest.TestCase):
    def test_verify(self):
        genesis_block = Block(0, "Genesis Block", "0")
        new_block = Block(1, "More data", genesis_block.hash)
        self.assertTrue(verify(new_block, genesis_block))

        new_block.hash = 'wrong'
        self.assertFalse(verify(new_block, genesis_block))

    def test_NotImplemented(self):
        blockchain = Chain()
        blockchain.append(Block(0, "Genesis Block", "0"))
        with self.assertRaises(NotImplementedError):
            del blockchain[0]
