Volume Breakout Scanner

Team Members:
Edward Platonov – eplatono@stevens.edu
Ardit Cana – acana@stevens.edu

Course:
EE 551 – Engineering in Python
Stevens Institute of Technology

This project implements a rolling volume breakout scanner for financial time-series data and evaluates whether intraday volume spikes can be used as a technical indicator to support trading decisions. Sudden increases in trading volume often reflect heightened market interest, which may precede meaningful price movement. The program detects these events in a realistic rolling manner and evaluates their usefulness through a simple trading simulation.

The scanner operates by computing a rolling average of trading volume and identifying breakout events when current volume exceeds a defined threshold relative to recent history. These breakouts are treated as technical signals that indicate abnormal market activity. The model was tested across multiple holding intervals, ranging from short intraday horizons to multi-week periods. Based on empirical testing, a 16-trading-day holding period produced the most realistic and consistent results, aligning with a typical swing-trading time frame.

The program is organized using a modular structure. The main analysis is executed through a Jupyter Notebook that runs the breakout detection and profit simulation. Supporting functionality is implemented in separate Python modules, including classes for stock data handling, volume analysis, and plotting. Unit tests are included using Pytest to verify core breakout detection logic. All data used in the project is publicly available and included in the repository for reproducibility.

Historical intraday stock data at a one-hour resolution was obtained from Yahoo Finance for CrowdStrike Holdings, Inc. (CRWD). The dataset is stored locally and loaded by the program to perform all analysis. Profit calculations are reported on a per-share basis and do not include transaction costs, leverage, or position sizing. This allows the strategy’s behavior to be evaluated independently of capital assumptions.

This project is intended as a foundational demonstration of Python engineering concepts learned in EE 551, including object-oriented design, data processing, visualization, generators, exception handling, and testing. While the trading model itself is intentionally simple, the framework can be easily extended to incorporate additional technical indicators, risk management rules, or more advanced decision-making techniques.

Contributions:
- Edward Platonov; volume breakout scanner, trading simulation logic, analysis workflow
- Ardit Cana; data, data handling, testing structures, plotting, documentation support
