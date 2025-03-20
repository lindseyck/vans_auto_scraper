# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:13:46 2025

@author: LKOSINSKI

UPDATE FILE NAME IN LINE 174 WITH EACH RUN
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Chrome WebDriver using webdriver-manager
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# List of all product categories to scrape - Comment in and out as needed
CATEGORY_URLS = [
    # "https://vansauto.com/product-category/antenna-related",
    # "https://vansauto.com/product-category/arm-rests-and-bases",
    # "https://vansauto.com/product-category/battery-trays-and-kits",
    # "https://vansauto.com/product-category/body-plug-kits",
    # "https://vansauto.com/product-category/brake-related",
    # "https://vansauto.com/product-category/bumper-and-related",
    # "https://vansauto.com/product-category/cat-whiskers",
    # "https://vansauto.com/product-category/clips-fasteners-cables-grommets-gaskets",
    # "https://vansauto.com/product-category/console-and-shifter",
    # "https://vansauto.com/product-category/dash-knobs-and-switches",
    # "https://vansauto.com/product-category/truck-charger-vans",
    # "https://vansauto.com/product-category/door-hardware",
    # "https://vansauto.com/product-category/door-sill-plates",
    # "https://vansauto.com/product-category/electrical",
    # "https://vansauto.com/product-category/electrical-switches-relays-locks",
    # "https://vansauto.com/product-category/emblems",
    # "https://vansauto.com/product-category/engine-and-drivetrain-related",
    # "https://vansauto.com/product-category/exhaust-manifolds-and-parts",
    # "https://vansauto.com/product-category/exterior-door-handles",
    # "https://vansauto.com/product-category/exterior-trim",
    # "https://vansauto.com/product-category/firewall-gasket-kits",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related/pump-to-carb-lines",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related/fuel-tanks",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related/gas-caps",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related/other",
    # "https://vansauto.com/product-category/fuel-tank-sending-units-and-related/sending-units",
    # "https://vansauto.com/product-category/gauges",
    # "https://vansauto.com/product-category/glove-box",
    # "https://vansauto.com/product-category/grilles-and-headlights",
    # "https://vansauto.com/product-category/headliners",
    # "https://vansauto.com/product-category/hinges-latches-locks-and-springs",
    # "https://vansauto.com/product-category/hood-and-firewall-pads",
    # "https://vansauto.com/product-category/insulation",
    # "https://vansauto.com/product-category/interior-and-exterior-mirrors",
    # "https://vansauto.com/product-category/interior-door-handles-and-window-cranks",
    # "https://vansauto.com/product-category/interior-light-and-trim-ash-trays",
    # "https://vansauto.com/product-category/interior-panels",
    # "https://vansauto.com/product-category/interior-trim",
    # "https://vansauto.com/product-category/misc-exterior-lights-license-plate-and-backup",
    # "https://vansauto.com/product-category/paint-gasket-kits",
    # "https://vansauto.com/product-category/park-lights",
    # "https://vansauto.com/product-category/pedal-pads-break-gas-clutch-and-break",
    # "https://vansauto.com/product-category/radiator-and-related",
    # "https://vansauto.com/product-category/screw-kits",
    # "https://vansauto.com/product-category/seals-window-hood-door-trunk-roof-and-body",
    # "https://vansauto.com/product-category/seat-related-belt-latches-and-knob",
    # "https://vansauto.com/product-category/sheet-metal-and-body-fender-parts",
    # "https://vansauto.com/product-category/steering-and-suspension", 
    # "https://vansauto.com/product-category/steering-column-and-turn-signal",
    # "https://vansauto.com/product-category/sun-visors",
    # "https://vansauto.com/product-category/taillights-and-bezels-side-markers",
    # "https://vansauto.com/product-category/transmission",
    # "https://vansauto.com/product-category/trunk-mats-and-related",
    # "https://vansauto.com/product-category/underhood", 
    # "https://vansauto.com/product-category/used_parts",
    # "https://vansauto.com/product-category/windshield-and-rear-window-seals",
    # "https://vansauto.com/product-category/windshield-washer-and-related"
    # "https://vansauto.com/product-category/general-motors",
    # "https://vansauto.com/product-category/uncategorized"
]

# Store extracted data
data = []

# Function to scroll down until all products are loaded
def scroll_to_load_all_products():
    scroll_pause_time = 2  # Adjust if needed
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)  # Allow time for products to load

        # Calculate new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break  # Stop scrolling if no new products are loaded
        
        last_height = new_height

# Function to extract product details from a product page
def extract_product_details(product_url):
    driver.get(product_url)
    time.sleep(2)  # Allow time for the page to load
    
    try:
        # Find SKU
        sku_element = driver.find_element(By.CLASS_NAME, "sku")
        sku = sku_element.text.strip()

        # Find all product images
        images = driver.find_elements(By.CSS_SELECTOR, "div.woocommerce-product-gallery__image img")
        image_links = [img.get_attribute("src") for img in images]

        return sku, image_links
    except Exception as e:
        print(f"Error extracting product details from {product_url}: {e}")
        return None, []

# Iterate through each product category
for category_url in CATEGORY_URLS:
    driver.get(category_url)
    time.sleep(3)  # Allow time for initial page load

    # Extract category name
    category_name = category_url.rstrip('/').split('/')[-1]
    print(f"Scraping category: {category_name}")

    # Scroll to load all products
    scroll_to_load_all_products()
    time.sleep(2)  # Extra wait for full loading

    # Find all product links
    products = driver.find_elements(By.CSS_SELECTOR, "ul.products li.product a.woocommerce-LoopProduct-link")
    product_links = [p.get_attribute("href") for p in products]

    print(f"Total products found in {category_name}: {len(product_links)}")

    # Visit each product page
    for product_url in product_links:
        print(f"Scraping product: {product_url}")
        sku, image_links = extract_product_details(product_url)

        if sku and image_links:
            for img in image_links:
                data.append({
                    "SKU": sku,
                    "Image Link": img,
                    "Category": category_name,
                    "Product URL": product_url
                })

# Close Selenium WebDriver
driver.quit()

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Save to CSV - CHANGE FILE NAME EACH RUN
df.to_csv("C:/Users/lkosinski/OneDrive - Bentley University/Documents/My MSBA/MA 795 Spring 2025/Vans Auto Parts Images/vansauto_products.csv", index=False)

print("Scraping completed. Data saved to csv.")
