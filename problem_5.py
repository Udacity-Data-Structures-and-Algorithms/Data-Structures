import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    """
    A class to represent a blockchain.

    Attributes:
    -----------
    chain : list[Block]
        The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Blockchain object.
        """
        self.chain: list[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (the first block in the blockchain).
        """
        # Genesis block has no previous hash and empty data
        genesis_block = Block(datetime.datetime.now(), "Genesis Block", "0")
        self.chain.append(genesis_block)


    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.

        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        previous_hash = self.chain[-1].hash
        new_block = Block(datetime.datetime.now(), data, previous_hash)
        self.chain.append(new_block)


    def __repr__(self) -> str:
        """
        Return a string representation of the blockchain.

        Returns:
        --------
        str
            A string representation of the blockchain.
        """
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

if __name__ == "__main__":
    def test_block_creation():
        print("\nTest Case 1: Block Creation")
        block = Block(datetime.datetime.now(), "Test Data", "0")
        assert block.data == "Test Data", "Block data not set correctly"
        assert block.previous_hash == "0", "Previous hash not set correctly"
        assert isinstance(block.hash, str) and len(block.hash) == 64, "Invalid hash format"
        print("✓ Block creation tests passed")

    def test_blockchain_basics():
        print("\nTest Case 2: Basic Blockchain Operations")
        blockchain = Blockchain()
        blockchain.add_block("Block 1")
        blockchain.add_block("Block 2")
        blockchain.add_block("Block 3")

        assert len(blockchain.chain) == 4, "Chain length incorrect"
        assert blockchain.chain[0].data == "Genesis Block", "Genesis block data incorrect"
        assert all(block.previous_hash == prev_block.hash 
                  for prev_block, block in zip(blockchain.chain, blockchain.chain[1:])), "Block linking failed"
        print("✓ Basic blockchain operations passed")

    def test_edge_cases():
        print("\nTest Case 3: Edge Cases")
        blockchain = Blockchain()
        
        # Test empty data
        blockchain.add_block("")
        assert blockchain.chain[-1].data == "", "Empty string handling failed"
        
        # Test special characters
        special_data = "!@#$%^&*()"
        blockchain.add_block(special_data)
        assert blockchain.chain[-1].data == special_data, "Special characters handling failed"
        
        # Test very long data
        long_data = "x" * 1000
        blockchain.add_block(long_data)
        assert blockchain.chain[-1].data == long_data, "Long data handling failed"
        print("✓ Edge cases passed")

    def test_hash_consistency():
        print("\nTest Case 4: Hash Consistency")
        blockchain = Blockchain()
        blockchain.add_block("Test Block")
        original_hash = blockchain.chain[-1].hash
        
        # Verify hash doesn't change for same data
        new_hash = blockchain.chain[-1].calc_hash()
        assert original_hash == new_hash, "Hash inconsistency detected"
        
        # Verify different data produces different hashes
        block1 = Block(datetime.datetime.now(), "Data1", "0")
        block2 = Block(datetime.datetime.now(), "Data2", "0")
        assert block1.hash != block2.hash, "Different data produced same hash"
        print("✓ Hash consistency tests passed")

    # Run all tests
    test_block_creation()
    test_blockchain_basics()
    test_edge_cases()
    test_hash_consistency()
    print("\nAll test cases passed successfully!")

