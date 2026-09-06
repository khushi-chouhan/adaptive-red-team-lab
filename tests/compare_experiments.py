import json


def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def get_security_results(experiment):
    if "tests" in experiment:
        return [
            test for test in experiment["tests"]
            if test["type"] == "security"
        ]

    results = []

    if experiment["test_1"]["type"] == "security":
        results.append(experiment["test_1"])

    if experiment["test_2"]["type"] == "security":
        results.append(experiment["test_2"])

    return results


def calculate_metrics(tests):
    failures = [
        test for test in tests
        if test["evaluation"]["result"] == "FAIL"
    ]

    return {
        "security_tests": len(tests),
        "failures": len(failures),
        "passes": len(tests) - len(failures),
        "failure_rate": len(failures) / len(tests) if tests else 0
    }


if __name__ == "__main__":

    baseline = load_json(
        "results/experiment_003_baseline.json"
    )

    adaptive = load_json(
        "results/experiment_002_adaptive.json"
    )

    baseline_tests = get_security_results(baseline)
    adaptive_tests = get_security_results(adaptive)

    baseline_metrics = calculate_metrics(baseline_tests)
    adaptive_metrics = calculate_metrics(adaptive_tests)

    print("=== Experiment Comparison ===")

    print("\nNon-Adaptive Baseline")
    print(f"Security tests: {baseline_metrics['security_tests']}")
    print(f"Failures: {baseline_metrics['failures']}")
    print(f"Passes: {baseline_metrics['passes']}")
    print(f"Failure rate: {baseline_metrics['failure_rate']:.2f}")

    print("\nAdaptive Experiment")
    print(f"Security tests: {adaptive_metrics['security_tests']}")
    print(f"Failures: {adaptive_metrics['failures']}")
    print(f"Passes: {adaptive_metrics['passes']}")
    print(f"Failure rate: {adaptive_metrics['failure_rate']:.2f}")

    print("\nAdaptation occurred:")
    print(adaptive["adaptation_occurred"])
