# Job Vacancy & Wage Data Visualizer

An interactive Python-based tool designed to filter, analyze, and visualize Canadian labor market statistics. This program processes job vacancy and wage data, allowing users to compare trends across different job sectors and education levels between 2015 and 2023.

## Project Contributors
* **Lorenzo Rodriguez** 
* **Elliot Peracchia** 
* **Owen Pitcher-Bond** 



## Features
* Toggle between searching for Job Vacancy totals or Average Wage data.
* Choose from 12 job categories.
* Filter data based on 7 education levels.
* Generates a Matplotlib graph showing trends over time, with a specific highlight on the chosen year.
* Automatically generates an `output.csv` containing the filtered results for further analysis.

## Prerequisites
The script requires Python 3 and the following libraries:
* **NumPy**: For data array handling.
* **Matplotlib**: For generating the visual graphs.

## Usage

1. Run the program:

```bash
python3 data_visualization.py Job_Vacancies_Quarterly.csv Average_Hourly_Wage_Quarterly.csv
```

2. Navigate through the program using the instructions printed in the terminal.
  
3. View the graph in the output window that is generated.

4. Open `output.csv` for further analysis of your filter selections.

## Additional Info:
This project is for educational purposes.
