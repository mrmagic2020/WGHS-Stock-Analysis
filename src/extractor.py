import pandas as pd


class StockDataExtractor:
    """
    A class used to extract and filter stock data from a CSV file.

    Attributes:
        file_path (str): The path to the CSV file containing stock data.
        df (pandas.DataFrame): The DataFrame containing the loaded stock data.

    Methods:
        load_data():
            Loads the stock data from the CSV file into a DataFrame.

        filter_by_sector(sector: str):
            Filters the loaded stock data by the specified sector.
    """

    def __init__(self, file_path="Approved trading - Equities.csv"):
        """
        Constructs all the necessary attributes for the StockDataExtractor object.

        Args:
            file_path (str): The path to the CSV file containing stock data. Defaults to "Approved trading - Equities.csv".

        Raises:
            TypeError: If file_path is not a string.
        """
        if not isinstance(file_path, str):
            raise TypeError("file_path must be a string")
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Loads the stock data from the CSV file into a DataFrame.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is empty or could not be parsed.
            RuntimeError: If an unexpected error occurs while loading the data.
        """
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"The file {self.file_path} is empty.")
        except pd.errors.ParserError:
            raise ValueError(f"The file {self.file_path} could not be parsed.")
        except Exception as e:
            raise RuntimeError(
                f"An unexpected error occurred while loading the data: {e}"
            )

    def get_unique_sectors(self):
        """
        Returns a list of unique sectors in the loaded stock data.

        Returns:
            list: A list of unique sectors.

        Raises:
            ValueError: If data is not loaded.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return self.df["GICS Sector"].unique()

    def filter_by_sector(self, sector: str):
        """
        Filters the loaded stock data by the specified sector.

        Args:
            sector (str): The sector to filter by.

        Returns:
            pandas.DataFrame: A DataFrame containing the filtered stock data.

        Raises:
            TypeError: If sector is not a string.
            ValueError: If data is not loaded.
        """
        if not isinstance(sector, str):
            raise TypeError("sector must be a string")
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        filtered_df = self.df[self.df["GICS Sector"] == sector]
        return filtered_df


def fetch_sector_data(sector: str):
    """
    Fetches stock data filtered by the specified sector.

    Args:
        sector (str): The sector to filter by.

    Returns:
        pandas.DataFrame: A DataFrame containing the filtered stock data.

    Raises:
        TypeError: If sector is not a string.
        ValueError: If data is not loaded or sector is not found.
        RuntimeError: If an unexpected error occurs.
    """
    if not isinstance(sector, str):
        raise TypeError("sector must be a string")

    try:
        extractor = StockDataExtractor()
        extractor.load_data()
        filtered_data = extractor.filter_by_sector(sector)

        if filtered_data.empty:
            raise ValueError(f"No data found for sector: {sector}")

        return filtered_data
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        raise RuntimeError(f"An error occurred while fetching sector data: {e}")
