from openai import OpenAI
from config import config

class OpenAIAdapter:
    def __init__(self, config) -> None:
        """
        Initialize the OpenAIAdapter with the given configuration.

        Args:
            config (BaseSettings): The configuration object containing the OpenAI API key.
        """
        self.client = OpenAI(api_key=config.openai_api_key.get_secret_value())

    def get_response(self, system_instructions: str, user_input: str) -> str:
        """
        Get a response from OpenAI based on the given instructions and user input.

        Args:
            system_instructions (str): The system instructions for OpenAI.
            user_input (str): The user's input.

        Returns:
            str: The response from OpenAI.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_instructions},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.7,
                max_tokens=256,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error interacting with OpenAI: {e}")
            return "An error occurred while processing your request."