def test_set_keeper(vesting_wallet, accounts, dev_msig):
    vesting_wallet.setKeeper(accounts[4], {"from": dev_msig})
