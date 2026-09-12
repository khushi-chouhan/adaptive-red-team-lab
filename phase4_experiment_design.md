# Phase 4 Experiment Design

## Research Question

Can feedback from previous security tests improve the efficiency of automated red-team testing of an AI agent?

## Objective

Compare adaptive and non-adaptive security testing under controlled conditions to determine whether feedback-driven test selection can improve vulnerability discovery efficiency.

## Experimental Conditions

### Non-Adaptive Condition

The system executes a predefined sequence of security tests.

The next test does not depend on the result of the previous test.

### Adaptive Condition

The system evaluates each test result and uses feedback to select the next security test.

The next test therefore depends on information obtained from the previous test.

## Test Categories

1. Direct instruction override
2. Rephrased instruction override
3. Authority-based instruction
4. Indirect instruction
5. Context manipulation
6. Benign request

## Controlled Agent

The agent will remain a local simulated agent during Phase 4.

The simulated agent will have multiple controlled behavioral outcomes so that different security tests can produce different results.

The simulated protected information will be synthetic test data.

## Primary Metric

### Tests to Vulnerability Discovery

The number of security tests executed before the first simulated vulnerability is discovered.

Lower values indicate more efficient discovery.

## Secondary Metrics

- Security-test failure rate
- Number of vulnerabilities discovered
- Test diversity
- Adaptation decisions
- Consistency across repeated trials

## Experimental Control

Adaptive and non-adaptive testing will use the same test budget and the same underlying simulated agent behavior.

Repeated trials will be used before making conclusions about effectiveness.

## Hypothesis

### H1

Feedback-driven adaptive testing will discover simulated vulnerabilities using fewer security tests than non-adaptive testing under controlled conditions.

### H0

Feedback-driven adaptive testing will not reduce the number of security tests required for vulnerability discovery compared with the non-adaptive approach.

## Limitations

- The agent is simulated rather than a real LLM.
- Agent behavior is deterministic during the initial experiments.
- The security outcomes are synthetic.
- The test set is small.
- Results from this environment cannot be generalized directly to real AI agents.

## Expected Research Contribution of Phase 4

Phase 4 is intended to establish a stronger experimental methodology for evaluating adaptive red-team test selection.

The goal is not to claim that adaptive red teaming is already superior, but to create a controlled environment in which that question can be tested.

## Experiment 008: Improved Adaptive Test Selection

Experiment 007 demonstrated that the initial feedback-driven selection policy successfully changed subsequent test selection, but it did not improve vulnerability-discovery efficiency compared with the non-adaptive control.

Experiment 008 will therefore investigate a more structured adaptive selection policy.

Instead of considering only the result of the immediately preceding test, the adaptive system will maintain information about previous test outcomes and use this accumulated feedback to prioritize remaining security-test categories.

The test catalog, controlled agent behavior, test budget, evaluation mechanism, and security objectives will remain unchanged. The primary experimental change will be the adaptive selection policy.

### Experiment 008 Research Question

Can accumulated feedback from previous security tests improve the efficiency of adaptive red-team test selection compared with a non-adaptive testing strategy?

### Experiment 008 Hypothesis

H1: An adaptive test-selection policy that uses accumulated feedback will discover simulated vulnerabilities using fewer security tests than the non-adaptive control under controlled conditions.

H0: An adaptive test-selection policy that uses accumulated feedback will not reduce the number of security tests required for vulnerability discovery compared with the non-adaptive control.

### Experimental Approach

Experiment 008 will use multiple controlled trials to compare the adaptive and non-adaptive conditions.

The non-adaptive condition will continue to execute a predefined sequence of tests.

The adaptive condition will maintain a history of previous test outcomes and use that information to prioritize the next available security test.

The same test budget and underlying simulated agent behavior will be used for both conditions.

Results will be recorded automatically so that discovery efficiency, vulnerability counts, failure rates, and adaptive decisions can be compared across trials.

### Methodological Rationale

The purpose of Experiment 008 is not to force an improvement in adaptive testing performance. If the improved adaptive policy does not outperform the non-adaptive control, that result will be recorded as evidence about the limitations of the tested policy and experimental environment.

The experiment is intended to strengthen the evaluation of feedback-driven red-team test selection through controlled comparison and repeated experimentation.
