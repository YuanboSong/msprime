#create a MCP for agentic AI systems
import langgraph as lg
from langgraph.agents import AgenticSystem
from langgraph.mcp import MultiComponentProtocol
class AgenticAIMCP(MultiComponentProtocol):
    def __init__(self, name: str, description: str, agents: list[AgenticSystem]):
        super().__init__(name=name, description=description, components=agents)

    def run_protocol(self, input_data):
        results = {}
        for agent in self.components:
            result = agent.process(input_data)
            results[agent.name] = result
        return results
# Example usage:
if __name__ == "__main__":
    # Define some agentic AI systems (placeholders)
    class SimpleAgent(AgenticSystem):
        def process(self, input_data):
            return f"Processed by {self.name}: {input_data}"

    agent1 = SimpleAgent(name="Agent 1")
    agent2 = SimpleAgent(name="Agent 2")

    # Create the MCP
    mcp = AgenticAIMCP(
        name="Agentic AI MCP",
        description="A protocol for coordinating agentic AI systems.",
        agents=[agent1, agent2]
    )

    # Run the protocol
    input_data = "Sample input"
    output = mcp.run_protocol(input_data)
    print(output) 