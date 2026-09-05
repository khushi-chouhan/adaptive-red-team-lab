class LocalAgent:
    def __init__(self):
        self.name = "LocalTestAgent"

    def respond(self, prompt):
        return f"Agent received: {prompt}"


if __name__ == "__main__":
    agent = LocalAgent()

    response = agent.respond("Hello, agent!")

    print(response)
