from brownie import config, MockV3Aggregator, network, accounts
from web3 import Web3

# setting static variables so that every value is parameterized.
DECIMALS = 8
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]


def get_account():  # for live chain
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():  # for a mock/development chain
    account = get_account()
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": account}
        )
    print("Mocks Deployed!")
