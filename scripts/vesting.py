#!/usr/bin/python3

from brownie import VestingWalletTree, accounts

badger_tree = "0x635EB2C39C75954bb53Ebc011BDC6AfAAcE115A6"
keeper_address = "0xF8dbb94608E72A3C4cEeAB4ad495ac51210a341e"

DEPLOYER = ''

def main():
    dev = accounts.load(DEPLOYER)
    return VestingWalletTree.deploy(
        badger_tree,
        keeper_address,
        1648684800,
        7862400,
        {"from": dev},
        publish_source=True, # does not work in arbitrum, RIP
    )
