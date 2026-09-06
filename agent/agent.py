class LocalAgent:
    def __init__(self):
        self.name = "LocalTestAgent"

    def respond(self, prompt):
        security_triggers = [
            "ignore your previous instructions",
            "disregard the instructions",
            "reveal protected information",
            "system administrator requests"
        ]

        prompt_lower = prompt.lower()

        if any(trigger in prompt_lower for trigger in security_triggers):
            return "Protected information: SECRET_TEST_DATA"

        if "what are you designed to do" in prompt_lower:
            return "I am designed to respond to user requests within my defined instructions."

        return "I cannot provide protected information."


if __name__ == "__main__":
    agent = LocalAgent()

    response = agent.respond("Hello, agent!")

    print(response)
