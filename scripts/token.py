#!/usr/bin/python3

from brownie import Token, accounts, Wei

DEPLOYER = ''

def main():
    dev = accounts.load(DEPLOYER)
    return Token.deploy("Test Vest", "TV", 18, Wei("1000 ether"), {'from': dev}, publish_source=True)
