from tests.scenarios import SCENARIOS
from tests.test_catalog import TEST_CASES


def load_scenario(scenario_name):
    test_lookup = {
        test["name"]: test
        for test in TEST_CASES
    }

    if scenario_name not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_name}")

    scenario_tests = []

    for test_name in SCENARIOS[scenario_name]:
        if test_name not in test_lookup:
            raise ValueError(
                f"Test '{test_name}' is not in the test catalog."
            )

        scenario_tests.append(test_lookup[test_name])

    return scenario_tests


if __name__ == "__main__":
    for scenario_name in SCENARIOS:
        tests = load_scenario(scenario_name)

        print(f"\n=== {scenario_name} ===")

        for test in tests:
            print(test["name"])
