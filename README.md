# News Correlation Analysis 10Academy week0

## Overview
This project is about analyzing news data to find out the correlation between news and various global media agencies. The project is implemented using Python programming language and the libraries used are pandas, matplotlib and spacy for NER (Name Entity Recognition).

## Data
The data used in this project is a news dataset from Kaggle. The dataset contains news articles from various global media agencies.

## Installation
### Creating a Virtual Environment
#### Using Conda

If Conda is your preferred package manager:

1. Open your terminal or command prompt.


2. Navigate to the project directory.
    ```bash
    cd path/to/news-correlation
   ```

3. Run the following commands to create a new virtual environment.

    ```bash
    conda create --name env_name python=3.12
    ```
    Replace ```env_name``` with the desired name of the virtual environment and ```3.12``` with your preferred Python version.


4. Activate the virtual environment.

    ```bash
    conda activate env_name
   ```

#### Using Virtualenv

```bash
virtualenv news_correlation
source news_correlation/bin/activate
```

### Installing Required Libraries

```bash
pip install -r requirements.txt
```

## Usage
### Configuration
The configuration file (```config.py```) contains the configuration parameters used in the project.
To modify the configuration parameters, edit the ```config.py``` file.

You can change the following parameters, including the directory paths to the data files and the output directory:
- ```news_data_path```: Directory to the news data file
- ```domains_path```: Directory to the domains data file
- ```traffic_path```: Directory to the traffic data file
- ```output_dir```: Directory to save the output files

### Data Loading
The package provides a data loader module (```loader.py```) to load the news data from a CSV file.

Example usage in main script (```main.py```):
```python
from src.loader import DataLoader

# Initialize DataLoader object
data_loader = DataLoader()

news_data = data_loader.load_news_data()
```

## Testing
The package provides a test module (```test.py```) to run unit tests on the implemented functions.

To run the tests, execute the following command:
```bash
make test
```

## Documentation
The package provides a documentation module (```docs.py```) to generate documentation for the implemented functions.

To generate the documentation, execute the following command:
```bash
make docs
```

## License
This project is licensed under the MIT License.




