from mm_zksync import abi


def test_zksync_contract_abi():
    res = abi.zksync_contract_abi()
    assert res[0]["name"] == "BlockCommit"
    assert res[-1]["name"] == "upgradeProposalHash"
