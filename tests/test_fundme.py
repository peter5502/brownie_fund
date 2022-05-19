from scripts.deploy import deploy, get_account
import pytest


def testfundwith():
    account = get_account()
    fundme = deploy()
    price = fundme.price()
    ent_fee = 10 / price
    tx = fundme.fund({"from": account, "value": ent_fee})
    tx.wait(1)
    assert fundme.checkbalance() == ent_fee
    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)
    assert fundme.checkbalance() == 0
