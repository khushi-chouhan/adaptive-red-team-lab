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
