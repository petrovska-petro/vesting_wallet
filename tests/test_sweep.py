from brownie import reverts


def test_sweep_no_rights(vesting_wallet, token, keeper):
    with reverts():
        vesting_wallet.sweepAll(token, {"from": keeper})


def test_sweep_rights(vesting_wallet, token, dev_msig):
    assert token.balanceOf(dev_msig) == 0

    vesting_wallet.sweepAll(token, {"from": dev_msig})

    assert token.balanceOf(dev_msig) == 0
