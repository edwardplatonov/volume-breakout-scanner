## Volume Breakout Scanner

Team Members:
- Edward Platonov – eplatono@stevens.edu
- Ardit Cana – acana@stevens.edu

## Course:
EE 551 – Engineering in Python
Stevens Institute of Technology

## Program Structure
This project implements a volume breakout scanner by simulating breakout evaluations in the running time of a given stock's historical data using a rolling volume method. It evaluates whether intraday volume spikes can be used as a technical indicator to support trading decisions. Sudden increases in trading volume often reflect heightened market interest, which may indicate significant price action. The program detects these events in a realistic rolling manner and evaluates their usefulness through a simple trading simulation. For this project, the group sampled 1-hour data from Yahoo Finance for CrowdStrike Holdings, Inc. (CRWD). The dataset is stored locally and loaded by the program to perform all analyses. Profit calculations are reported on a per-share basis and do not include transaction costs, leverage, or position sizing. This is for simplicity and performance evaluation to indicate feasibility.

The scanner operates by computing a rolling average of trading volume and identifying breakout events when current volume exceeds a defined threshold relative to recent history. These breakouts are treated as technical signals that indicate abnormal market activity. The model was tested across multiple holding intervals, ranging from short intraday periods (i.e. 1 hour) to multi-week periods (i.e. 3 weeks). Based on testing, a 16-trading-day holding period produced the most realistic and consistent results, aligning with a typical swing-trading time frame.

The program is organized using a modular structure. The main analysis is executed through a Jupyter Notebook that runs the breakout detection and profit simulation. Supporting functionality is implemented in separate Python modules, including classes for stock data handling, volume analysis, and plotting. Unit tests are included using Pytest to verify core breakout detection logic. All data used in the project is publicly available and included in the repository for reproducibility.

## How to Run
To use the program, the required Python libraries should be installed first. Unit tests can be executed by running pytest from the project root directory. The main analysis is performed by opening the Jupyter Notebook file and running all cells from top to bottom. The first cell detects and visualizes volume breakouts, while the second cell simulates a long-only trading strategy and reports performance statistics.

This project is intended as a foundational demonstration of Python engineering concepts learned in EE 551, including object-oriented design, data processing, visualization, generators, exception handling, and testing. While the trading model itself is intentionally simple, the framework can be easily extended to incorporate additional technical indicators, risk management rules, or more advanced decision-making techniques and even machine learning algorithms.

## Contributions:
- Edward Platonov: volume breakout scanner, trading simulation logic, analysis workflow
- Ardit Cana: data, data handling, testing structures, plotting, documentation support





