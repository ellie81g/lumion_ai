# from web3 import Web3

# # rpc url от куда брать данные по транзам 
# RPC_URL = "https://mainnet.base.org"  

# web3 = Web3(Web3.HTTPProvider(RPC_URL))

# def get_transaction_count(wallet_address):
#     try:
#         checksum_address = web3.to_checksum_address(wallet_address)
#         tx_count = web3.eth.get_transaction_count(checksum_address)
#         return tx_count
#     except Exception as e:
#         return f"invalid address: {e}"

# # Рандируем транзы --> risk lvl
# def calculate_risk_level(tx_count):
#     if tx_count == 0:
#         return 0
#     elif 1 <= tx_count <= 10:
#         return 4
#     elif 11 <= tx_count <= 60:
#         return 7
#     elif 61 <= tx_count <= 125:
#         return 16
#     elif 126 <= tx_count <= 200:
#         return 24
#     elif 201 <= tx_count <= 500:
#         return 31
#     elif 501 <= tx_count <= 1500:
#         return 42
#     elif 1501 <= tx_count <= 40000:
#         return 49
#     else:
#         return "N/A (Out of range)"  # На случай если там больше 40к транз

# if __name__ == "__main__":
#     wallet = input("Enter wallet address: ").strip()
#     tx_count = get_transaction_count(wallet)

#     if tx_count is None:
#         print("Invalid wallet address. Please try again.")
#     else:
#         risk_level = calculate_risk_level(tx_count)
#         print(f"Transaction count for {wallet}: {tx_count}")
#         print(f"Risk Level: {risk_level}")

import random


risk_level = random.randint(1,49)