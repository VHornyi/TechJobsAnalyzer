# TechJobsAnalyzer: Web Scraping from NoFluffJobs, Data Analysis, and Machine Learning for Job Market Insights

## Description
This project is focused on web scraping, data processing, analysis, and machine learning. It extracts job postings from the NoFluffJobs platform, processes and stores the data in a structured format, and performs data analysis and predictive modeling to uncover insights about job trends, salaries, and technologies.

## Project Structure
```
TechJobsAnalyzer
|
├── Analysis and ML
│   ├── DecisionTreeRegressor.ipynb
│   ├── jobs_data_analysis.ipynb
│   ├── nofluffjobs_Dec24.csv
│   ├── prepared_nofluffjobs_Dec24.csv
│
├── Data
│   ├── nofluffjobs.csv
│   ├── prepared_nofluffjobs.csv
│   ├── vacancies.db
│
├── Parser
│   ├── main.py
│
├── SQL DB
│   ├── csv_to_sqlite.py
│   ├── db_checker.py
│
├── readme.md
├── requirements.txt
```

## Features

### 1. **Web Scraping (main.py)**
- **Goal**: Extract job postings from the NoFluffJobs platform.
- **Key Functions**:
  - `parse_jobs(url, max_items)`: Scrapes job postings and saves them to a CSV file.
  - `extract_job_link`, `extract_job_title`, `extract_location`, `extract_salary`, `extract_technologies`, `extract_company_name`, and `get_seniority`: Helper functions to extract specific fields from the job postings.
- **Output**: A CSV file `nofluffjobs.csv` in the `Data` folder.

### 2. **Data Storage (csv_to_sqlite.py)**
- Converts the CSV file into a SQLite database for structured data storage.
- Creates a `vacancies` table in `vacancies.db` with columns for job title, location, salary, technologies, company, seniority, and job link.

### 3. **Database Validation (db_checker.py)**
- Retrieves and displays the last 5 entries from the `vacancies` table for validation.

### 4. **Data Analysis (jobs_data_analysis.ipynb)**
- **Steps**:
  - Data loading, cleaning, and preparation for analysis.
  - Exploratory data analysis to identify trends and patterns.
  - **Goals**:
    - 📊 **Technology Popularity**: Explore trends and demand for different technologies.
    - 💰 **Salary Analysis**: Compare compensation for various roles and skills.
    - 🔍 **Correlation Analysis**: Discover patterns between variables.
    - 📈 **Data Visualization**: Graphical representation of key insights.

### 5. **Machine Learning (DecisionTreeRegressor.ipynb)**
- Implements a Decision Tree Regressor for predictive modeling.
- **Goal**: Predict salaries listed in job postings based on factors such as location, company, required key technologies, etc.
- **Steps**:
  - Splitting data into training and test sets.
  - Hyperparameter tuning using `GridSearchCV` and cross-validation.
  - Evaluating model performance with metrics such as MAE, MSE, and R².
  - Visualizing actual vs predicted salaries.

## Prerequisites
- Python 3.7+
- Google Chrome and ChromeDriver (for Selenium)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/VHornyi/TechJobsAnalyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TechJobsAnalyzer
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Run the Parser
To scrape job postings from NoFluffJobs and save them to a CSV file:
```bash
python Parser/main.py
```

### 2. Convert CSV to SQLite Database
To create a SQLite database from the scraped CSV:
```bash
python SQL DB/csv_to_sqlite.py
```

### 3. Validate Database
To check the last 5 entries in the database:
```bash
python SQL DB/db_checker.py
```

### 4. Analyze Data
Open `jobs_data_analysis.ipynb` in Jupyter Notebook to:
- Clean and prepare data.
- Perform exploratory data analysis.
- Visualize trends and insights.

### 5. Train and Evaluate ML Model
Open `DecisionTreeRegressor.ipynb` in Jupyter Notebook to:
- Train a Decision Tree Regressor.
- Evaluate and optimize model performance.

## Contributions
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
