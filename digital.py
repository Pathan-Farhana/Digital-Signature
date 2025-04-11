from py_ecc.bls import G2ProofOfPossession as bls
from py_ecc.optimized_bls12_381 import curve_order
import os

# Simulate multiple clients
NUM_CLIENTS = 3
clients = []

# Generate keys for each client
for i in range(NUM_CLIENTS):
    sk = int.from_bytes(os.urandom(32), 'big') % curve_order
    pk = bls.SkToPk(sk)
    clients.append({'sk': sk, 'pk': pk})

# The message all clients will sign
message = b"Transaction approved"
print(f"\nMessage being signed: {message.decode()}\n")

# Each client signs and verifies
for i, client in enumerate(clients):
    print(f"--- Client {i+1} ---")
    
    # Sign the message
    signature = bls.Sign(client['sk'], message)
    signature_hex = signature.hex()
    print(f"Signature at signing     : {signature_hex}")

    # Verify the signature
    is_valid = bls.Verify(client['pk'], message, signature)
    print(f"Signature used in verify : {signature_hex}")
    print(f"Signature valid?         : {is_valid}\n")
