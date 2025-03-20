### README.md
```md
# Vans Auto Scraper

This repository contains Python scripts for scraping automotive parts images from Vans Auto’s website and consolidating the scraped data into a single CSV file.

## Features
- Scrapes product images, SKUs, and categories from Vans Auto’s website.
- Saves extracted data in CSV format.
- Merges multiple CSV files into one dataset for analysis.

## Installation
Clone the repository:
```sh
git clone https://github.com/lindseyck/vans-auto-scraper.git
cd vans-auto-scraper
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Step 1: Scrape Product Images
Modify the `CATEGORY_URLS` list in `01_scrape_vans_auto_parts_images.py` to specify which product categories to scrape, then run:
```sh
python 01_scrape_vans_auto_parts_images.py
```
This script will extract SKUs, product URLs, and image links, saving them as a CSV file.

### Step 2: Union CSV Files
Run:
```sh
python 02_union_vans_auto_parts_images_files.py
```
This script consolidates all CSV files into `vans_auto_parts_images.csv`.

## Requirements
- Python 3.x
- Selenium
- WebDriver Manager
- Pandas

