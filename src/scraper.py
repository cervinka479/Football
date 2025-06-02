import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from config import config
from match import Match
from file_handler import FileHandler


class Scraper:
    def __init__(self, config) -> None:
        """
        Initialize the Scraper with the given configuration.
        """
        self.config = config

    def scrape_matches(self, url: str) -> list[Match]:
        """
        Entry method to scrape football match data from the given URL.

        Args:
            url (str): The URL to scrape.

        Returns:
            List[Match]: A list of Match objects.
        """
        try:
            soup = self._fetch_page(url)
            sections = self._get_sections(soup)
            matches = []

            for section in sections:
                competition = self._extract_competition(section)
                match_count = self._calculate_match_count(section)

                for u in range(match_count):
                    match = self._extract_match_details(section, u, competition)
                    if match:
                        matches.append(match)

            return matches
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error during scraping: {e}")
            return []

    def _fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetch the webpage content and parse it with BeautifulSoup.

        Args:
            url (str): The URL to fetch.

        Returns:
            BeautifulSoup: Parsed HTML content.
        """
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def _get_sections(self, soup: BeautifulSoup) -> list[BeautifulSoup]:
        """
        Locate the sections containing match data.

        Args:
            soup (BeautifulSoup): Parsed HTML content.

        Returns:
            List[BeautifulSoup]: A list of sections containing match data.
        """
        return soup.find_all("section")[0].find_all("main")[0].find_all("div")[0].find_all("div")[6].find_all("section")

    def _extract_competition(self, section: BeautifulSoup) -> str:
        """
        Extract the competition name from a section.

        Args:
            section (BeautifulSoup): A section containing match data.

        Returns:
            str: The competition name.
        """
        try:
            if section.find_all("header"):
                competition_element = section.find_all("header")[0].find_all("div")[1].find_all("a")[0].get_text(strip=True)
                return re.sub(r"[^a-zA-Z0-9\-\.,]", "", competition_element)  # Clean competition name
        except Exception as e:
            print(f"Error extracting competition name: {e}")
        return ""

    def _calculate_match_count(self, section: BeautifulSoup) -> int:
        """
        Calculate the number of matches in a section.

        Args:
            section (BeautifulSoup): A section containing match data.

        Returns:
            int: The number of matches.
        """
        try:
            return int(len(section.find_all("main")[0].find_all("div")) / 10)
        except Exception as e:
            print(f"Error calculating match count: {e}")
            return 0

    def _extract_match_details(self, section: BeautifulSoup, index: int, competition: str) -> Match:
        """
        Extract match details for a specific match.

        Args:
            section (BeautifulSoup): A section containing match data.
            index (int): The index of the match in the section.
            competition (str): The competition name.

        Returns:
            Match: A Match object containing the match details.
        """
        try:
            yesterday = datetime.now() - timedelta(days=1)
            date = yesterday.strftime("%Y-%m-%d")

            home_team = section.find_all("main")[0].find_all("div")[index * 10].find_all("a")[0].find_all("div")[2].get_text(strip=True)
            away_team = section.find_all("main")[0].find_all("div")[index * 10].find_all("a")[0].find_all("div")[5].get_text(strip=True)
            home_score = section.find_all("main")[0].find_all("div")[index * 10].find_all("div", recursive=False)[1].find_all("span")[0].get_text(strip=True)
            away_score = section.find_all("main")[0].find_all("div")[index * 10].find_all("div", recursive=False)[1].find_all("span")[1].get_text(strip=True)

            return Match(date, competition, home_team, away_team, home_score, away_score)
        except Exception as e:
            print(f"Error extracting match details for match {index + 1}: {e}")
            return None
        
if __name__ == "__main__":
    file_handler = FileHandler(config)
    scraper = Scraper(config)
    match_data = scraper.scrape_matches(config.football_base_url)
    file_handler.save_matches_to_json(match_data)
