import json

from agent.agent import LocalAgent
from tests.evaluator import evaluate_response
from tests.test_catalog import TEST_CASES


def run_test(test_case):
    agent = LocalAgent()

    response = agent.respond(test_case["prompt"])

    evaluation = evaluate_response(
        test_case["type"],
        test_case["prompt"],
        response
    )

    return {
        "name": test_case["name"],
        "type": test_case["type"],
        "prompt": test_case["prompt"],
        "response": response,
        "evaluation": evaluation
    }


def calculate_metrics(results):
    security_tests = [
        result for result in results
        if result["type"] == "security"
    ]

    failures = [
        result for result in security_tests
        if result["evaluation"]["result"] == "FAIL"
    ]

    return {
        "tests_executed": len(results),
        "security_tests": len(security_tests),
        "vulnerabilities_discovered": len(failures),
        "failure_rate": (
            len(failures) / len(security_tests)
            if security_tests else 0
        )
    }


if __name__ == "__main__":

    results = []

    for test_case in TEST_CASES:
        result = run_test(test_case)
        results.append(result)

        print(f"\n=== {result['name']} ===")
        print(f"Prompt: {result['prompt']}")
        print(f"Response: {result['response']}")
        print(f"Evaluation: {result['evaluation']['result']}")

    metrics = calculate_metrics(results)

    experiment = {
        "experiment": "Experiment 005",
        "condition": "non_adaptive",
        "title": "Phase 4 Non-Adaptive Control",
        "objective": (
            "Establish a non-adaptive control condition using "
            "a predefined sequence of security tests."
        ),
        "adaptive": False,
        "test_budget": len(TEST_CASES),
        "tests": results,
        "metrics": metrics
    }

    with open(
        "results/experiment_005_non_adaptive.json",
        "w"
    ) as file:
        json.dump(experiment, file, indent=2)

    print("\n=== Experiment Saved ===")
    print("results/experiment_005_non_adaptive.json")

    print("\n=== Metrics ===")
    print(f"Tests executed: {metrics['tests_executed']}")
    print(
        f"Vulnerabilities discovered: "
        f"{metrics['vulnerabilities_discovered']}"
    )
    print(f"Failure rate: {metrics['failure_rate']:.2f}")
