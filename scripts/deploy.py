from brownie import accounts, Fundme, network, config, MockV3Aggregator
import os
from web3 import Web3

FORKED = ["mainnet-fork-dev"]
LOCAL_CHAIN = ["development", "ganache-cli"]


def deploy():
    account = get_account()
    if network.show_active() not in LOCAL_CHAIN:
        pricefeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        pricefeed = MockV3Aggregator.deploy(
            18, Web3.toWei(2000, "ether"), {"from": account}
        )
    fund_contract = Fundme.deploy(
        pricefeed,
        {"from": account},
        publish_source=False,
    )
    print(network.show_active())
    print(fund_contract)
    return fund_contract


def get_account():
    if network.show_active() in LOCAL_CHAIN or network.show_active in FORKED:
        return accounts[0]
    else:
        # print(config["wallet"][network.show_active()]["from_key"])
        return accounts.add(os.getenv("PRIVATE_KEY"))


def main():
    deploy()
