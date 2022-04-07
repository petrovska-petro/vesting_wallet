#!/usr/bin/python3

import pytest

HALF_H = 1800


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def gov(accounts):
    return accounts.at('0x292549E6bd5a41aE4521Bb8679aDA59631B9eD4C', force=True)

@pytest.fixture(scope="module")
def keeper(accounts):
    return accounts[1]

@pytest.fixture(scope="module")
def tree(accounts):
    return accounts.at('0xF8dbb94608E72A3C4cEeAB4ad495ac51210a341e', force=True)

@pytest.fixture(scope="module")
def dev_msig(accounts):
    return accounts[3]


@pytest.fixture(scope="module")
def token(ERC20PresetFixedSupply, gov):
    return ERC20PresetFixedSupply.deploy("Test Token", "TST", 1e21, gov, {"from": gov})


@pytest.fixture(scope="module")
def vesting_wallet(chain, VestingWallet, token, tree, gov, keeper, dev_msig):
    vesting = VestingWallet.deploy(
        tree, keeper, chain[-1].timestamp, HALF_H, {"from": gov}
    )

    token.transfer(vesting, token.balanceOf(gov), {"from": gov})

    return vesting_wallet
