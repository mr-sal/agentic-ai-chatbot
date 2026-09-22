import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_agent(user_message):
    """Send a user message to the AI agent and return the response."""

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=(
            "You are an intelligent business and productivity AI agent. "
            "Understand the user's request, reason about the task, "
            "and provide a clear, useful response."
        ),
        input=user_message
    )

    return response.output_text


if __name__ == "__main__":
    print("Agentic AI Chatbot")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_agent(user_input)
        print(f"Agent: {answer}\n")