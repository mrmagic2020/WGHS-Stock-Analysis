import yfinance as yf


class StockMetricsFetcher:
    """
    A class to fetch stock metrics using yfinance.
    """

    def __init__(self, ticker: str):
        """
        Initializes the StockMetricsFetcher with a stock ticker.

        Args:
            ticker (str): The ticker symbol of the stock.
        """
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def fetch_basic_metrics(self):
        try:
            stock_info = self.stock.info

            # Ensure the stock info has valid data
            if not stock_info:
                raise ValueError(
                    f"Ticker {self.ticker} does not exist or has no available data."
                )

            # Fetch financial data and handle if 'Total Revenue' is not available
            financials = self.stock.financials
            if "Total Revenue" in financials.index:
                revenue_data = financials.loc["Total Revenue"]

                # Revenue values over the years
                revenue_2023 = revenue_data.iloc[0] if len(revenue_data) > 0 else None
                revenue_2018 = revenue_data.iloc[5] if len(revenue_data) > 5 else None
                revenue_2020 = revenue_data.iloc[3] if len(revenue_data) > 3 else None

                # Calculate CAGR for 5 years (if data is available)
                if revenue_2023 and revenue_2018:
                    cagr_5 = ((revenue_2023 / revenue_2018) ** (1 / 5)) - 1
                else:
                    cagr_5 = None

                # Calculate CAGR for 3 years (if data is available)
                if revenue_2023 and revenue_2020:
                    cagr_3 = ((revenue_2023 / revenue_2020) ** (1 / 3)) - 1
                else:
                    cagr_3 = None

                # Calculate combined CAGR only if both 5-year and 3-year CAGR are available
                if cagr_5 is not None and cagr_3 is not None:
                    combined_cagr = cagr_3 * 0.3 + cagr_5 * 0.7
                elif cagr_5 is not None:
                    combined_cagr = cagr_5
                elif cagr_3 is not None:
                    combined_cagr = cagr_3
                else:
                    combined_cagr = "N/A"
            else:
                # Handle the case where 'Total Revenue' does not exist
                cagr_5 = None
                cagr_3 = None
                combined_cagr = None

            metrics = {
                "Ticker": self.ticker,
                "Company": stock_info.get("longName"),
                "Exchange": stock_info.get("exchange"),
                "EPS": stock_info.get("trailingEps"),
                "P/E": stock_info.get("trailingPE"),
                "Beta": stock_info.get("beta"),
                "Debt to Equity": stock_info.get("debtToEquity"),
                "P/B": stock_info.get("priceToBook"),
                "EV/EBITDA": stock_info.get("enterpriseToEbitda"),
                "ROE": stock_info.get("returnOnEquity"),
                "ROA": stock_info.get("returnOnAssets"),
                "Gross Profit Margin": stock_info.get("grossMargins"),
                "Revenue Growth Rate": stock_info.get("revenueGrowth"),
                "CAGR (5 years)": cagr_5,
                "CAGR (3 years)": cagr_3,
                "CAGR": combined_cagr,
            }

            # Replace None values with "N/A" for CSV compatibility
            for key, value in metrics.items():
                if value is None:
                    metrics[key] = "N/A"

            return metrics

        except Exception as e:
            # If an error occurs (e.g., ticker not found), return an error message or log it
            print(f"Error fetching data for {self.ticker}: {e}")
            return None


# Example of how to use this class
if __name__ == "__main__":
    # Example ticker
    ticker = "TSLA"

    # Instantiate the fetcher
    fetcher = StockMetricsFetcher(ticker)

    # Fetch the metrics and print them
    metrics = fetcher.fetch_basic_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value}")
