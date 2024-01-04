# SQL Query Generator

This is a web application built using Streamlit, enabling users to generate SQL queries from plain English instructions. It utilizes a custom AI library (`genai`) to interpret user input and provide the corresponding SQL query along with the expected output and an explanation of its function.

## Tech Stack

- **Streamlit**: Framework for building the web interface.
- **Custom AI Library (`genai`)**: Interfaces with Google's Generative AI model for SQL query generation.
- **dotenv**: Handles sensitive information by loading from a `.env` file.

## Functionality

- Accepts plain English input to generate SQL queries.
- Utilizes the AI model to convert text into SQL queries.
- Displays the resulting SQL query, expected query output (table data), and an explanation of query function.

## Usage

1. Clone this repository.
2. Set up the environment by installing required dependencies.
3. Ensure the `.env` file contains the necessary API keys.
4. Run the `app.py` file.
5. Input your plain English query description and click "Generate SQL Query" to see the output and explanation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/sql-query-generator.git
