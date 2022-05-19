from scripts.deploy import get_account
from brownie import Fundme, network, config, MockV3Aggregator


def fund():
    fundme = Fundme[-1]
    account = get_account()
    price = fundme.price()
    ent_fee = 10 / price
    print("Entrance fee in ether is", ent_fee)
    fundme.fund({"from": account, "value": ent_fee})
    print(fundme.checkbalance())


def withdraw():
    account = get_account()
    fundme = Fundme[-1]
    fundme.withdraw({"from": account})
    print(fundme.checkbalance())


def main():
    fund()
    withdraw()
