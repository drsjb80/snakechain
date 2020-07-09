import hashlib
import datetime
import unittest

# based on https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

def hash(block):
    sha256 = hashlib.sha256()
    sha256.update(str(block.index).encode('utf-8') + \
        str(block.timestamp).encode('utf-8') + \
        str(block.data).encode('utf-8') + \
        str(block.previous_hash).encode('utf-8'))
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

class Chain:
    def __init__(self):
        self.blockchain = []
        genesis_block = Block(0, 'Genesis Block', '0')
        self.blockchain.append(genesis_block)

    def __str__(self):
        ret = ''
        for block in self.blockchain:
            ret += str(block)
        return ret

    def append(self, whattoappend):
        new_block=Block(len(self.blockchain), whattoappend, self.blockchain[-1:][0].hash)
        self.blockchain.append(new_block)

if '__main__' == __name__:
    blockchain = Chain()
    while True:
        whattodo = input('(a)ppend (p)rint (q)uit: ' )
        if whattodo == 'a' or whattodo == 'append':
            blockchain.append(input('enter the string to append: '))
        elif whattodo == 'p' or whattodo == 'print':
            print(blockchain)
        elif whattodo == 'q' or whattodo == 'quit':
            break;

class TestSnakeChain(unittest.TestCase):
    def test_verify(self):
        genesis_block = Block(0, "Genesis Block", "0")
        new_block = Block(1, "More data", genesis_block.hash)
        self.assertTrue(verify(new_block, genesis_block))

        new_block.hash = 'wrong'
        self.assertFalse(verify(new_block, genesis_block))
