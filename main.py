from details import get_brand, get_brand_cars, get_car_variants, extract_variant_details
from db import create_database, create_table
from concurrent.futures import ThreadPoolExecutor

create_database()
create_table()

url = "https://www.carwale.com/"

MAX_THREADS = 10

def process_variant(variant):
    try:
        print(f"    Variant: {variant['variant_name']}")
        extract_variant_details(variant)
    except Exception as e:
        print(f"Error: {e}")

for brand in get_brand(url):
    print(f"Processing Brand: {brand['brand_name']}")

    for car in get_brand_cars(brand["brand_url"], brand["brand_name"]):
        print(f"  Car: {car['car_name']}")

        variants = list(get_car_variants(car["car_url"], car))

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            executor.map(process_variant, variants)