import csv
from web3 import Web3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chains = {
    "Arbitrum": {
        "rpc_url": "https://arbitrum.llamarpc.com",
    },
    "Base": {
        "rpc_url": "https://base.llamarpc.com",
    },
    "zkSync": {
        "rpc_url": "https://mainnet.era.zksync.io",
    },
    "Ethereum": {
        "rpc_url": "https://eth.llamarpc.com",
    },
    # ... (you can add more chains here)
}

# Read wallet addresses from wallet.txt
with open("wallet.txt", "r") as file:
    QUERY_ADDRESSES = [Web3.to_checksum_address(line.strip()) for line in file.readlines()]

wallet_sums = {addr: {'ETH': 0} for addr in QUERY_ADDRESSES}

with open("allbalance.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Chain', 'Address', 'ETH Balance'])

    for query_address in QUERY_ADDRESSES:
        for chain_name, chain_data in chains.items():
            w3 = Web3(Web3.HTTPProvider(chain_data["rpc_url"]))

            # Query ETH balance for the query address
            eth_balance = w3.eth.get_balance(query_address)
            eth_human_readable = w3.from_wei(eth_balance, 'ether')

            # Log the ETH balance
            logging.info(f'ETH balance for {query_address} on {chain_name}: {eth_human_readable}')

            # Update wallet sums
            wallet_sums[query_address]['ETH'] += eth_human_readable

            # Write to CSV
            csv_writer.writerow([chain_name, query_address, eth_human_readable])

    # Calculate the total balance of all wallets
    total_eth_balance = sum(wallet_sums[addr]['ETH'] for addr in wallet_sums)

    # Log the total balance
    logging.info(f'Total ETH balance: {total_eth_balance}')

    # Append the total balance line to the CSV
    csv_writer.writerow(['Total', 'All Wallets', total_eth_balance])

    print(f"Total ETH Balance: {total_eth_balance}")

print("Script has completed successfully.")
