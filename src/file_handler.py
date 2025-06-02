from datetime import datetime
import os
import json
from typing import List
from match import Match
from config import config


class FileHandler:
    def __init__(self, config) -> None:
        """
        Initialize the FileHandler with the given configuration.
        """
        self.config = config

    def should_update_data(self) -> bool:
        """
        Check if the scraper should run based on the last run date.

        Returns:
            bool: True if data needs to be updated, False otherwise.
        """
        try:
            if os.path.exists(self.config.last_run_file):
                with open(self.config.last_run_file, "r") as file:
                    last_run_date: str = file.read().strip()
                    if last_run_date == datetime.now().strftime("%Y-%m-%d"):
                        return False  # Data is already up-to-date
            return True
        except Exception as e:
            print(f"Error checking last run date: {e}")
            return True  # Default to updating if there's an error

    def update_last_run_date(self) -> None:
        """
        Update the last run date to the current date.
        """
        try:
            os.makedirs(os.path.dirname(self.config.last_run_file), exist_ok=True)
            with open(self.config.last_run_file, "w") as file:
                file.write(datetime.now().strftime("%Y-%m-%d"))
        except Exception as e:
            print(f"Error updating last run date: {e}")

    def load_match_data(self) -> str:
        """
        Load match data from the JSON file.
        """
        try:
            with open(self.config.knowledge_base_path, "r", encoding="utf-8") as file:
                match_data = json.load(file)
                return json.dumps(match_data, ensure_ascii=False)
        except Exception as e:
            print(f"Error loading match data: {e}")
            return []

    def save_matches_to_json(self, matches: List[Match]) -> None:
        """
        Save a list of Match objects to a JSON file.
        """
        try:
            os.makedirs(os.path.dirname(self.config.knowledge_base_path), exist_ok=True)
            with open(self.config.knowledge_base_path, "w", encoding="utf-8") as file:
                json.dump([match.to_dict() for match in matches], file, indent=4, ensure_ascii=False)
            print(f"Matches successfully saved to {self.config.knowledge_base_path}")
        except Exception as e:
            print(f"Error saving matches to JSON: {e}")

if __name__ == "__main__":
    file_handler = FileHandler(config)
    print(file_handler.config.__dict__)