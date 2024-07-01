from web3 import Web3
from web3.middleware import geth_poa_middleware

from decouple import config

from .constants import CONTRACT_ADDRESS, CONTRACT_ABI, NETWORK_URL

web3 = Web3(Web3.HTTPProvider(NETWORK_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)


def complete_payment(payment_id):
    private_key = config("OWNER_PRIVATE_KEY")
    ownerAccount = web3.eth.account.from_key(private_key)

    # Create a transaction
    txn = contract.functions.completePayment(payment_id).build_transaction(
        {
            "from": ownerAccount.address,
            "nonce": web3.eth.get_transaction_count(ownerAccount.address),
        }
    )

    # Sign and send the transaction
    signed_txn = web3.eth.account.sign_transaction(
        txn, private_key=private_key
    )

    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Transaction hash: {tx_hash.hex()}")

    # Wait for the transaction to be mined
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction receipt:", tx_receipt)
    return tx_receipt


def get_payment(payment_id):
    payment = contract.functions.payments(payment_id).call()
    return payment

if __name__ == "__main__":
    get_payment("f6762ae1-5b18-44c4-9200-ef9ccd18004")
