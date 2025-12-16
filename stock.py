import pandas as pd

class Stock:
    """
    Represents a stock and its historical price and volume data.
    """
    # Required columns for valid stock data
    REQUIRED_COLUMNS = {"Datetime", "Open", "High", "Low", "Close", "Volume"}

    def __init__(self, dataframe: pd.DataFrame, symbol: str):
        """
        Initialize stock object with historical data and a ticker symbol (CRWD for this project)
        """
        self.symbol = symbol # store stock ticker symbol
        self.data = dataframe.copy() # work on copy
        
        # Validate data format and prepare datetime column
        self._validate_columns()
        self._parse_datetime()

    def _validate_columns(self):
        """
        Ensure that all required columns exist in the dataset
        """
        missing = self.REQUIRED_COLUMNS - set(self.data.columns) # find any missing required columns
        
        # Raise an error if required columns are missing
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    def _parse_datetime(self):
        """
        Convert the datetime column to pandas datetime and sort the data
        """
        self.data["Datetime"] = pd.to_datetime(self.data["Datetime"]) # convert datetime column to datetime objects
        self.data.sort_values("Datetime", inplace=True) # sort data chronologically
        self.data.reset_index(drop=True, inplace=True) # reset index after sorting

    def __str__(self):
        """
        Return summary of stock dataset
        """
        # Extract essential information
        start = self.data["Datetime"].iloc[0]
        end = self.data["Datetime"].iloc[-1]
        rows = len(self.data)

        # Return formatted summary
        return (f"Stock: {self.symbol}\n"
                f"Rows: {rows}\n"
                f"From: {start}\n"
                f"To:   {end}")