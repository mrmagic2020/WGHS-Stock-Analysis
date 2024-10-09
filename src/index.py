import csv
from pathlib import Path
from tqdm import tqdm
from yaspin import yaspin

from extractor import StockDataExtractor
from fetcher import StockMetricsFetcher


# Initialise StockDataExtractor
extractor = StockDataExtractor()
extractor.load_data()
SECTORS = extractor.get_unique_sectors()

# Define the headers for the CSV file
headers = [
    "Ticker",
    "Company",
    "Exchange",
    "EPS",
    "P/E",
    "Beta",
    "Debt to Equity",
    "P/B",
    "EV/EBITDA",
    "ROE",
    "ROA",
    "Gross Profit Margin",
    "Revenue Growth Rate",
    "CAGR (5 years)",
    "CAGR (3 years)",
    "CAGR",
]

# Create the results directory
Path("results").mkdir(exist_ok=True)

for sector in SECTORS:
    output_file = f"results/{sector}.csv"

    sector_stock_data = extractor.filter_by_sector(sector)
    sector_tickers = sector_stock_data["Ticker"].tolist()

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        with tqdm(
            total=len(sector_tickers), desc=f"Fetching data for {sector}", unit="stock"
        ) as pbar:
            for ticker in sector_tickers:
                with yaspin(text=f"Fetching {ticker}...", color="cyan") as spinner:
                    fetcher = StockMetricsFetcher(ticker)
                    metrics = fetcher.fetch_basic_metrics()

                    spinner.ok("✔")

                    if metrics:
                        row = [
                            metrics.get("Ticker", ""),
                            metrics.get("Company", ""),
                            metrics.get("Exchange", ""),
                            metrics.get("EPS", ""),
                            metrics.get("P/E", ""),
                            metrics.get("Beta", ""),
                            metrics.get("Debt to Equity", ""),
                            metrics.get("P/B", ""),
                            metrics.get("EV/EBITDA", ""),
                            metrics.get("ROE", ""),
                            metrics.get("ROA", ""),
                            metrics.get("Gross Profit Margin", ""),
                            metrics.get("Revenue Growth Rate", ""),
                            metrics.get("CAGR (5 years)", ""),
                            metrics.get("CAGR (3 years)", ""),
                            metrics.get("CAGR", ""),
                        ]

                        writer.writerow(row)

                pbar.update(1)
