import os
from datetime import datetime
from openai import OpenAI
from config import config
from file_handler import FileHandler
from openai_adapter import OpenAIAdapter
from scraper import Scraper


# Initialize FileHandler
file_handler = FileHandler(config)

# Initialize OpenAI client with API key
client: OpenAI = OpenAI(api_key=config.openai_api_key.get_secret_value())


def update_match_data(config, file_handler: FileHandler) -> None:
    """
    Check if match data needs to be updated and update it if necessary.

    Args:
        config: The configuration object.
        file_handler (FileHandler): The FileHandler instance for saving and loading data.
    """
    scraper = Scraper(config)

    if file_handler.should_update_data():
        print("Updating match data...")
        try:
            matches = scraper.scrape_matches(config.football_base_url)
            if matches:
                file_handler.save_matches_to_json(matches)
                file_handler.update_last_run_date()
                print("Match data updated successfully.")
            else:
                print("No matches found or an error occurred during scraping.")
        except Exception as e:
            print(f"Error updating match data: {e}")
    else:
        print("Match data is already up-to-date.")

def run_cli(openai_adapter: OpenAIAdapter, match_data: str) -> None:
    """
    Run the CLI for interacting with the OpenAI chatbot.

    Args:
        openai_adapter (OpenAIAdapter): The OpenAIAdapter instance.
        match_data (str): The match data to include in the system instructions.
    """
    system_instructions = f"""
    Jsi asistent fotbalového analytika. Odpovídej pouze v češtině, bez ohledu na jazyk otázky.
    Když bude chtít uživatel odejít a nebude vědět jak, řekni mu ať napíše do chatu "exit".
    Máš k dispozici pouze informace o zápasech, které se odehrály včera.
    Zde jsou data o zápasech, která můžeš použít při odpovídání:
    {match_data}
    """

    print("Ahoj, jsem fotbalový analitik! Napište 'exit' pro ukončení.")

    while True:
        user_input = input("Uživatel: ")

        if user_input.lower() == "exit":
            print("Sbohem!")
            break

        response = openai_adapter.get_response(system_instructions, user_input)
        print("ChatGPT:", response)


if __name__ == "__main__":
    file_handler = FileHandler(config)
    openai_adapter = OpenAIAdapter(config)

    update_match_data(config, file_handler)
    
    match_data = file_handler.load_match_data()
    run_cli(openai_adapter, match_data)