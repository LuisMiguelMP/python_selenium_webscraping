# Web Scraping with Python and Selenium

The code shows how to do web scraping using Python and Selenium.

We use as data the https://sbot.org.br/localize-o-ortopedista/ site to extract all the licensed orthopedists.  


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

What things you need to install the software and how to install them

* Python 3.x
* Chrome Driver (you can get it here: https://chromedriver.chromium.org/downloads)
* Some Python libraries following

## Installing

A step by step series of examples that tell you how to get a development env running

### Install the following Python libraries:

 * **selenium** - An API to write functional/acceptance tests using Selenium WebDriver.

With:
```
pip install -r requirements.txt
```

### Chrome Driver 

[You can find install instructions in the official repository.](https://chromedriver.chromium.org)
Remember, to run the project you'll need to update your drive location.
If you are on Windows, the current path is C:/chromedriver.exe by default.
On Linux/MacOS X, after download the respective driver, you'll need to update 'testcase\test_page.py' (line 8) and 'webscraping.py' - at project's root, line 12.


## Running the code

```
python webscraping.py
```

## Contributing

Feel free to submitting pull requests.


## License

This project is licensed under the [GNU General Public License](https://opensource.org/licenses/GPL-3.0).
