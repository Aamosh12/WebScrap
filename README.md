# Web Scraping Project: Bank Data Scraper

This project is a Python script that uses Selenium and Beautiful Soup to scrape bank data from the official website of Nepal Rastra Bank (NRB) at https://www.nrb.org.np/bank-list/. The scraped data is then processed and stored for further analysis or use.

## Getting Started

These instructions will help you set up and run the project on your local machine.

## Prerequisites

To run this project, you need to have the following software and tools installed on your computer:

- **Python 3.x**
- **Chrome or Firefox web browser**
- **Selenium WebDriver for Chrome or Firefox**
- **Python IDE:** You can choose any Python Integrated Development Environment (IDE) you prefer. Options include Visual Studio Code, PyCharm, or any other code editor that supports Python development.


## Installation

To get started with the project, follow these steps:

### Navigating to the Project Directory

1. Open your terminal or command prompt.

2. Clone the project repository to your local machine using the following command:

   `git clone git@github.com:Aamosh1/webScrap.git`

3. Change your current working directory to the project directory:

    `cd webScrap`

    You are now in the project directory and ready to proceed with the installation and usage instructions.

### Installing Dependencies

1. Install the required Python libraries and dependencies:

    `pip install -r requirements.txt`

2. (If required) Download the appropriate Selenium WebDriver for your browser (Chrome or Firefox) and place it in the project directory.


## Usage

1. Open the main.py file and update the BROWSER to 'chrome' or 'firefox' depending on the web browser you are using. (By default, The browser is chrome but you can change it on line 2 and 17)
2. Run the script to start scraping bank data:
   `python main.py` or if you are using pycharm or tool similar to this, you can find the run button.

## Configuration

If needed, you can configure the project by modifying variables in the main.py file. For example, you can change the output file name or path.

## Acknowledgments

- [Selenium](https://www.selenium.dev/): The web scraping framework used in this project, which greatly facilitated the data extraction process.

- [Nepal Rastra Bank (NRB)](https://www.nrb.org.np): The source of the bank data that is being scraped, without which this project would not be possible.

## Further Reading

Explore the following resources for more information and insights related to this project:

- [Selenium Documentation](https://www.selenium.dev/documentation/en/): Detailed documentation on using Selenium for web scraping and automated testing.

- [Nepal Rastra Bank Official Website](https://www.nrb.org.np/): Visit the official website of Nepal Rastra Bank (NRB) to stay updated with any changes in the website structure that may affect your web scraping.

- [Beautiful Soup Documentation](https://realpython.com/beautiful-soup-web-scraper-python/): Learn about Beautiful Soup, to build a web scraper with python.


Feel free to explore these resources to gain a deeper understanding of web scraping, the Beautiful Soup library and Selenium.
