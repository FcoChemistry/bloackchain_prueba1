import hashlib
import time

class Block:
  def __init__ (self,index, previous_hash, transactions, timestamp, nonce=0):
    self.index = index
    self.previous_hash = previous_hash
    self.transactions = transactions
    self.timestamp = timestamp
    self.nonce = nonce
    self.hash = self.calculate_hash()

  def calculate_hash(self):
    block_string = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}"
    return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        self.difficulty = 2  # Ajusta esto para cambiar la dificultad de minería

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block", time.time())
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def mine_block(self, transactions):
        last_block = self.get_latest_block()
        new_block = Block(last_block.index + 1, last_block.hash, transactions, time.time())

        while new_block.hash[:self.difficulty] != '0' * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(f"Block mined: {new_block.hash}")
        self.add_block(new_block)

  if __name__ == "__main__":
    simple_coin = Blockchain()

    print("Mining block 1...")
    simple_coin.mine_block("Transaction 1 Data")

    print("Mining block 2...")
    simple_coin.mine_block("Transaction 2 Data")

    print("Mining block 3...")
    simple_coin.mine_block("Transaction 3 Data")

    for block in simple_coin.chain:
        print(f"Block {block.index} [{block.timestamp}]: {block.transactions} - {block.hash}")
