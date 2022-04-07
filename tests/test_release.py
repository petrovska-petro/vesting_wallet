HALF_H = 1800


def test_release(chain, vesting_wallet, token, keeper, tree):
    # assert tree 0
    assert token.balanceOf(tree) == 0

    vesting_wallet.release(token, {"from": keeper})

    chain.sleep(HALF_H / 2)
    chain.mine()

    vesting_wallet.release(token, {"from": keeper})

    chain.sleep(HALF_H / 2)
    chain.mine()

    vesting_wallet.release(token, {"from": keeper})

    # assert tree
    total_supply = token.totalSupply()

    assert token.balanceOf(tree) == total_supply
