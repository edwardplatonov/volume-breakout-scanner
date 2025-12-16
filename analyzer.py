import pandas as pd

class VolumeAnalyzer:
    """
    Analyzes trading volume to detect intraday volume breakouts
    """
    def __init__(self, stock, window=20, multiplier=2.0):
        """
        Initialize the VolumeAnalyzer with rolling parameters
        """
        # Store stock object and analysis parameters
        self.stock = stock
        self.window = window
        self.multiplier = multiplier

        # Work on a copy of stock data to leave original untampered
        self.data = stock.data.copy()

    def compute_rolling_volume(self):
        """
        Compute rolling volume stats used for breakout detection
        """
        # Rolling mean of volume
        self.data["rolling_volume"] = (self.data["Volume"].rolling(self.window).mean())
        # Rolling standard deviation of volume
        self.data["rolling_std"] = (self.data["Volume"].rolling(self.window).std())
        # Rolling z-score of volume (relative spike strength)
        self.data["volume_zscore"] = ((self.data["Volume"] - self.data["rolling_volume"]) / self.data["rolling_std"])

    def breakout_generator(self):
        """
        Generator that provides where volume exceeds the rolling threshold
        """
        # Start scanning after enough data exists for rolling calculations
        i = self.window
        while i < len(self.data):
            current_vol = self.data.loc[i, "Volume"]
            avg_vol = self.data.loc[i, "rolling_volume"]
            # Check for volume breakout condition
            if current_vol > self.multiplier * avg_vol:
                yield i
            i += 1

    def detect_breakouts(self):
        """
        Detect volume breakouts and return the corresponding data rows
        """
        # Compute rolling statistics before scanning
        try:
            self.compute_rolling_volume()
        except KeyError as e:
            raise KeyError("Volume column missing from data") from e
        # Collect breakout indices from the generator
        breakout_indices = [i for i in self.breakout_generator()]
        # Return dataframe containing breakout rows
        return self.data.loc[breakout_indices]
