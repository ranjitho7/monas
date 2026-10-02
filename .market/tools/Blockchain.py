"""
Blockchain.py
=============
Blockchain (EVM) tools from Agno, as an independent @tool.

pip install agno web3
"""

import os
from agno.tools import tool


@tool
def evm_get_balance(address: str, rpc_url: str = "https://eth.llamarpc.com") -> str:
    """Get the native token balance of an EVM address.

    Args:
        address (str): The wallet address to check.
        rpc_url (str): The EVM RPC endpoint URL. Defaults to a public Ethereum RPC.
    """
    os.environ["EVM_RPC_URL"] = rpc_url
    from agno.tools.evm import EVMTools
    return EVMTools(rpc_url=rpc_url).get_balance(address)


@tool
def evm_get_transaction(tx_hash: str, rpc_url: str = "https://eth.llamarpc.com") -> str:
    """Get details of an on-chain transaction by hash.

    Args:
        tx_hash (str): The transaction hash.
        rpc_url (str): The EVM RPC endpoint URL. Defaults to a public Ethereum RPC.
    """
    os.environ["EVM_RPC_URL"] = rpc_url
    from agno.tools.evm import EVMTools
    return EVMTools(rpc_url=rpc_url).get_transaction(tx_hash)
