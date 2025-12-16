import matplotlib.pyplot as plt

def plot_volume_breakouts(stock, breakouts):
    """
    Plot price and volume and highlight breakout points
    """
    data = stock.data

    # Initialize figures
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Price plot
    ax1.plot(data["Datetime"], data["Close"], label="Close Price")
    ax1.scatter(breakouts["Datetime"], breakouts["Close"], color="red", s=10, label="Volume Breakout")
    ax1.set_ylabel("Price")
    ax1.legend()

    # Volume plot
    ax2.plot(data["Datetime"], data["Volume"], label="Volume", alpha=0.6)
    ax2.scatter(breakouts["Datetime"], breakouts["Volume"], color="red", s=10)
    ax2.set_ylabel("Volume")
    ax2.set_xlabel("Datetime")
    
    # Format
    plt.tight_layout()
    plt.show()