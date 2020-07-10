import hashlib
import datetime
import unittest

# based on https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.do_hash()

    def __str__(self):
        return 'Index: ' + str(self.index) + \
            '\nCreated: ' + str(self.timestamp) + \
            '\nData: ' + str(self.data) + \
            '\nHash: ' + str(self.hash) + '\n'

    def do_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str(self.index).encode('utf-8') + \
            str(self.timestamp).encode('utf-8') + \
            str(self.data).encode('utf-8') + \
            str(self.previous_hash).encode('utf-8'))
        return sha256.hexdigest()

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
        new_block = Block(len(self.blockchain), whattoappend, self.blockchain[-1:][0].hash)
        self.blockchain.append(new_block)

if '__main__' == __name__:
    blockchain = Chain()
    while True:
        whattodo = input('(a)ppend (p)rint (q)uit: ')
        if whattodo in ('a', 'append'):
            blockchain.append(input('enter the string to append: '))
        elif whattodo in ('p', 'print'):
            print(blockchain)
        elif whattodo in ('q', 'quit'):
            break

class TestSnakeChain(unittest.TestCase):
    def verify(self, block, previous):
        block_hash = hash(block)
        return block.hash == block_hash and previous.hash == block.previous_hash

    def test_verify(self):
        genesis_block = Block(0, "Genesis Block", "0")
        new_block = Block(1, "More data", genesis_block.hash)
        self.assertTrue(self.verify(new_block, genesis_block))

        new_block.hash = 'wrong'
        self.assertFalse(self.verify(new_block, genesis_block))
