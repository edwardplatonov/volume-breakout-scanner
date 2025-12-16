import pandas as pd
from stock import Stock
from analyzer import VolumeAnalyzer

def test_rolling_volume_computation():
    """
    Test that the rolling volume is computed correctly for a simple constant-volume dataset
    """
    # Create a simple dataset with constant volume
    data = pd.DataFrame({
        "Datetime": pd.date_range("2024-01-01", periods=5, freq="h"),
        "Open": [1, 1, 1, 1, 1],
        "High": [1, 1, 1, 1, 1],
        "Low": [1, 1, 1, 1, 1],
        "Close": [1, 1, 1, 1, 1],
        "Volume": [10, 10, 10, 10, 10],})

    # Initialize Stock and VolumeAnalyzer objects
    stock = Stock(data, "TEST")
    analyzer = VolumeAnalyzer(stock, window=2)
    analyzer.compute_rolling_volume() # compute rolling volume
    assert analyzer.data["rolling_volume"].iloc[2] == 10 # make sure rolling mean volume is correct

def test_breakout_detection():
    """
    Test that a single volume breakout is detected when volume exceeds the rolling threshold.
    """
    # Create dataset with one clear volume spike
    data = pd.DataFrame({
        "Datetime": pd.date_range("2024-01-01", periods=6, freq="h"),
        "Open": [1] * 6,
        "High": [1] * 6,
        "Low": [1] * 6,
        "Close": [1] * 6,
        "Volume": [10, 10, 10, 50, 10, 10],})

    # Initialize Stock and VolumeAnalyzer objects
    stock = Stock(data, "TEST")
    analyzer = VolumeAnalyzer(stock, window=3, multiplier=2)
    breakouts = analyzer.detect_breakouts() # detect breakouts
    assert len(breakouts) == 1 # amke sure exactly one breakout is found
