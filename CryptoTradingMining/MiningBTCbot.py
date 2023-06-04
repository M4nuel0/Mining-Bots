import hashlib
import time

NONCE_LIMIT = 100000000000

zeroes = 0000


def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith(str(0000)):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
    return 1

block_number = 24
transactions = "76123fcc2142"
previous_hash = "876de8756b967c87"

nonce_found = 16

combined_text = str(block_number) + transactions + previous_hash + str(nonce_found)

print(hashlib.sha256(combined_text.encode()).hexdigest())

mine(block_number, transactions, previous_hash)
    
