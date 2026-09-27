import hashlib
import time

import pytest


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def test_registration_and_preflight_replay_guard(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = direct_deploy("contracts/DynamicLearningPath.py")
    direct_vm.sender = direct_alice
    contract.create_program("academy", "Open Curriculum")
    contract.register_course(
        "academy", "fundamentals", "https://catalog.example/fundamentals", digest("fundamentals")
    )
    contract.register_course(
        "academy", "applications", "https://catalog.example/applications", digest("applications")
    )
    program = contract.get_program("academy")
    assert program["version"] == 0
    assert set(program["catalog"]) == {"fundamentals", "applications"}
    with direct_vm.expect_revert("exact catalog course permutation required"):
        contract.evaluate_path(
            "academy", "bad-order", "fundamentals,fundamentals", 0, program["root"], int(time.time()) + 300
        )
    with direct_vm.prank(direct_bob), direct_vm.expect_revert("program owner required"):
        contract.register_course(
            "academy", "extra", "https://catalog.example/extra", digest("extra")
        )
