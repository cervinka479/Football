# Football Match Data Scraper and Chatbot

This project is a football match data scraper and chatbot application. It fetches football match data from a website or an API, processes it, and allows users to interact with the data through a chatbot interface.

---

## Features

-   **Scraping Match Data**: Scrapes football match data from a website.
-   **Data Storage**: Saves match data in a JSON file for later use.
-   **Chatbot Interface**: Allows users to query match data through a chatbot that responds in Czech.
-   **Automatic Updates**: Automatically updates match data once per day to ensure the latest information is available.
-   **Detailed Match Information**: Includes competition name, teams, scores.

---

## Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## How to Run the Application

1. **Clone the Repository**:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Set Up API Keys**:

    - Replace the placeholder API key in `src/main.py` with your OpenAI API key.

3. **Run the Application**:

    - Navigate to the `src` folder:
        ```bash
        cd src
        ```
    - Run the main application:
        ```bash
        python main.py
        ```

4. **Chat with the Chatbot**:
    - The chatbot will greet you and allow you to ask questions about football matches.
    - Type your queries in Czech, and the chatbot will respond with relevant match data.
    - To exit the chatbot, type `exit`.

---

## How the Application Works

### 1. **Scraping Match Data**

-   The application scrapes match data from a website.
-   Match data includes:
    -   Date
    -   Competition
    -   Home and Away Teams
    -   Scores

### 2. **Automatic Updates**

-   The application checks if the match data is up-to-date by comparing the current date with the last run date stored in `data/last_run_date.txt`.
-   If the data is outdated, the scraper runs and updates the data in `data/scraped_matches.json`.

### 3. **Chatbot**

-   The chatbot uses OpenAI's GPT model to answer user queries about the match data.
-   It uses the latest match data stored in `data/scraped_matches.json`.

---

## File Structure

```
src/
├── main.py                # Main application entry point
├── scraper.py             # Web scraping logic
data/
├── scraped_matches.json  # JSON file storing scraped match data
└── last_run_date.txt     # File storing the last run date of the scraper
README.md                # Project documentation
requirements.txt         # Python dependencies
```

### WIP Folder

The `src/WIP` folder contains files that are currently under development and are **not intended for user usage**. These files may include experimental features or incomplete functionality.

---

## Example Usage

### Run the Chatbot

Run the chatbot by executing `main.py`:

```bash
python main.py
```

Example interaction:

```
Ahoj, jsem fotbalový analitik! Napište 'exit' pro ukončení.
Uživatel: Jaký byl výsledek zápasu mezi týmy X a Y?
ChatGPT: Zápas mezi týmy X a Y skončil 2:1.
Uživatel: exit
Sbohem!
```

---

## Notes

-   Ensure you have a valid OpenAI API key.
-   The application is designed to work with Czech-language queries.
-   Match data is updated automatically once per day.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.
