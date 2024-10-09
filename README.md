# WGHS Stock Analysis

This project fetches and analyses stock market data for different sectors based on publicly available financial metrics. It uses Yahoo Finance to extract metrics such as EPS, P/E Ratio, ROE, CAGR, and more for each stock within a sector.

## Prerequisites

To run this project locally, ensure you have the following installed:

- Python 3.x

- Git (optional - for cloning the repository)

You can install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

## Installation

 1. Clone the repository:

    ```bash
    git clone https://github.com/mrmagic2020/WGHS-Stock-Analysis.git
    cd WGHS-Stock-Analysis
    ```

    Alternatively, manually download the repository.

 2. Install dependencies:

    Run the following command to install the necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

    The main libraries used in the project are:

    - pandas: for handling and processing CSV data.

    - yfinance: for fetching stock metrics from Yahoo Finance.

    - tqdm: for displaying progress bars.

    - yaspin: for displaying a loading spinner while fetching data.

## Running the Code

1. Approved Trading List

    Ensure you have the Approved trading - Equities.csv file in the root directory. This file is provided along with this repository.

2. Extract and Fetch Stock Data

    To fetch the financial metrics for stocks in different sectors, run the main script:

    ```bash
    python src/index.py
    ```

    The script will:

    - Extract unique sectors from the Approved trading - Equities.csv file.

    - Fetch financial metrics for stocks in each sector using Yahoo Finance.

    - Save the results in CSV files inside the results/ directory, one CSV per sector.

    If you want to stop the script at any time, press `Ctrl + C`. The script will save the fetched data up to that point.

3. Output

    The results are saved as CSV files in the `results/` directory. Each file contains data for stocks in a particular sector, with the following metrics:

    - Ticker
    - Company
    - Exchange
    - EPS
    - P/E Ratio
    - Beta
    - Debt to Equity
    - P/B Ratio
    - EV/EBITDA
    - ROE
    - ROA
    - Gross Profit Margin
    - Revenue Growth Rate
    - CAGR (5 years)
    - CAGR (3 years)
    - Combined CAGR

## Source Code Explanation

The source code is well-documented. Here is a brief overview of the main files:

### index.py

The main script that orchestrates the entire process:

1. Extract: Extracts unique sectors from the stock list using extractor.py.

2. Fetch: Fetches financial metrics for each stock in a sector using fetcher.py.

3. Save: Saves the fetched metrics into CSV files, one for each sector.

### extractor.py

Responsible for loading the stock data from the CSV file and filtering stocks by sector.

- `load_data()`: Loads the CSV file into a DataFrame.

- `get_unique_sectors()`: Returns the unique sectors from the loaded data.

- `filter_by_sector()`: Filters the data for a specific sector.

### fetcher.py

Fetches stock metrics from Yahoo Finance using the yfinance library.

- `fetch_basic_metrics()`: Retrieves financial data such as EPS, P/E ratio, ROE, and CAGR for a given stock ticker.

### Requirements File

The requirements.txt file contains the necessary Python packages for the project. Make sure to install them by running:

```bash
pip install -r requirements.txt
```

## Troubleshooting

- Data fetching errors: If a particular stock ticker returns None or causes an error, it might be due to missing data on Yahoo Finance for that ticker. These errors are handled gracefully, and the script will continue fetching data for the remaining tickers.

- Missing CSV file: Ensure that the Approved trading - Equities.csv file is available in the root directory of the project. If not, the script will raise a FileNotFoundError.

## Contributions

Feel free to fork this repository, submit issues, or create pull requests if you want to contribute to this project.
