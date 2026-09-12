import json

from agent.agent import LocalAgent
from tests.evaluator import evaluate_response
from tests.feedback import analyze_result
from tests.scenario_loader import load_scenario
from tests.scenarios import SCENARIOS


TEST_BUDGET = 5


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


def choose_adaptive_test(feedback, remaining_tests):
    if not remaining_tests:
        return None

    if feedback["vulnerable"]:
        preferred_test = "Authority-Based Instruction"
    else:
        preferred_test = "Indirect Instruction"

    for test in remaining_tests:
        if test["name"] == preferred_test:
            return test

    return remaining_tests[0]


def calculate_metrics(results):
    security_tests = [
        result for result in results
        if result["type"] == "security"
    ]

    failures = [
        result for result in security_tests
        if result["evaluation"]["result"] == "FAIL"
    ]

    first_vulnerability = None

    for index, result in enumerate(results, start=1):
        if result["evaluation"]["result"] == "FAIL":
            first_vulnerability = index
            break

    return {
        "tests_executed": len(results),
        "security_tests": len(security_tests),
        "vulnerabilities_discovered": len(failures),
        "failure_rate": (
            len(failures) / len(security_tests)
            if security_tests else 0
        ),
        "tests_to_vulnerability_discovery": first_vulnerability
    }


def run_non_adaptive(scenario_name):
    tests = load_scenario(scenario_name)

    selected_tests = tests[:TEST_BUDGET]

    results = []

    for test in selected_tests:
        results.append(run_test(test))

    return results


def run_adaptive(scenario_name):
    remaining_tests = load_scenario(scenario_name)

    results = []
    adaptation_decisions = []

    while remaining_tests and len(results) < TEST_BUDGET:

        if not results:
            selected_test = remaining_tests[0]

            decision = {
                "previous_test": None,
                "feedback_used": False,
                "selected_test": selected_test["name"]
            }

            adaptation_decisions.append(decision)

        else:
            feedback = analyze_result(
                results[-1]["response"]
            )

            selected_test = choose_adaptive_test(
                feedback,
                remaining_tests
            )

            decision = {
                "previous_test": results[-1]["name"],
                "feedback_used": True,
                "vulnerable": feedback["vulnerable"],
                "next_action": feedback["next_action"],
                "selected_test": (
                    selected_test["name"]
                    if selected_test else None
                )
            }

            adaptation_decisions.append(decision)

        if selected_test is None:
            break

        remaining_tests.remove(selected_test)

        results.append(run_test(selected_test))

    return results, adaptation_decisions


def run_experiment():

    experiment_results = {}

    for scenario_name in SCENARIOS:

        print("\n==============================")
        print(scenario_name)
        print("==============================")

        non_adaptive_results = run_non_adaptive(
            scenario_name
        )

        adaptive_results, adaptation_decisions = run_adaptive(
            scenario_name
        )

        non_adaptive_metrics = calculate_metrics(
            non_adaptive_results
        )

        adaptive_metrics = calculate_metrics(
            adaptive_results
        )

        experiment_results[scenario_name] = {
            "non_adaptive": {
                "tests": non_adaptive_results,
                "metrics": non_adaptive_metrics
            },
            "adaptive": {
                "tests": adaptive_results,
                "adaptation_decisions": adaptation_decisions,
                "metrics": adaptive_metrics
            }
        }

        print(
            "Non-adaptive tests to vulnerability:",
            non_adaptive_metrics[
                "tests_to_vulnerability_discovery"
            ]
        )

        print(
            "Adaptive tests to vulnerability:",
            adaptive_metrics[
                "tests_to_vulnerability_discovery"
            ]
        )

    experiment = {
        "experiment": "Experiment 007",
        "title": "Multi-Scenario Adaptive vs Non-Adaptive Comparison",
        "objective": (
            "Compare adaptive and non-adaptive security testing "
            "across multiple controlled scenarios."
        ),
        "test_budget": TEST_BUDGET,
        "scenarios": experiment_results
    }

    with open(
        "results/experiment_007_phase4_comparison.json",
        "w"
    ) as file:
        json.dump(experiment, file, indent=2)

    print("\n=== Experiment Saved ===")
    print("results/experiment_007_phase4_comparison.json")


if __name__ == "__main__":
    run_experiment()
