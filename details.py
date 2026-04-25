from lxml import html
import json
from urllib.parse import urljoin
import time
from db import insert_into_db
from models import CarDetails
from request import request

base_url = "https://www.carwale.com/"

# ---------------- SAFE REQUEST ----------------
def find_json(url):
    try:
        res = request(url)

        tree = html.fromstring(res)

        script = tree.xpath('//script[contains(text(),"__INITIAL_STATE__")]/text()')

        if not script:
            print(f"No JSON: {url}")
            return None

        script_text = script[0]
        json_str = script_text[script_text.find('{'):script_text.rfind('}')+1]

        return json.loads(json_str)

    except Exception as e:
        print(f"Error: {url} -> {e}")
        return None


# ---------------- BRAND ----------------
def get_brand(url):
    data = find_json(url)
    if not data:
        return

    for m in data.get('homePage', {}).get('makeList', []):
        name = m.get('maskingName', '')
        if name:
            yield {
                "brand_name": name,
                "brand_url": urljoin(base_url, f"{name}-cars/")
            }


# ---------------- CARS ----------------
def get_brand_cars(brand_url, brand_name):
    data = find_json(brand_url)
    if not data:
        return

    for m in data.get('makePage', {}).get('models', []):
        car = m.get('rootMaskingName', '')
        if car:
            yield {
                "brand_name": brand_name,
                "brand_url": brand_url,
                "car_name": car,
                "car_url": urljoin(brand_url, car + "/")
            }


# ---------------- VARIANTS ----------------
def get_car_variants(car_url, car_info):
    data = find_json(car_url)
    if not data:
        return

    for t in data.get('modelPage', {}).get('trimSummary', []):
        variant = t.get('trimMaskingName', '')
        if variant:
            yield {
                **car_info,
                "variant_name": variant,
                "variant_url": urljoin(car_url, variant + "/")
            }


# ---------------- DETAILS ----------------
def extract_variant_details(variant):
    data = find_json(variant["variant_url"])
    if not data:
        return

    details = data.get('trimPage', {}).get('specsFeaturesMaster', [])

    highlights, specifications, safety, features = [], [], [], []

    for section in details:
        name = section.get('name', '').lower()

        if name in ["highlights", "hightlights"]: 
            for s in section.get('subCategories', []): 
                for item in s.get('highLights', {}).get('addedInNext', []): 
                    highlights.append(item.get('itemName', '').strip())
        # -------- HIGHLIGHTS --------
        # if name in ["highlights", "hightlights"]:
        #     for s in section.get('subCategories', []):
        #         hl = s.get('highLights', {})
        #         for key in ["segmentBest", "addedInCurrent", "addedInNext"]:
        #             for item in hl.get(key, []):
        #                 highlights.append(item.get('itemName', '').strip())

        # -------- SPECIFICATIONS --------
        elif "specification" in name:
            for s in section.get('subCategories', []):
                temp = []
                for i in s.get('items', []):
                    k = i.get('itemName', '').strip()
                    v = i.get('value', '').strip()
                    if k:
                        temp.append({"key": k, "value": v})

                specifications.append({
                    "key": s.get('name', ''),
                    "value": temp
                })

        # -------- SAFETY --------
        elif "safety" in name:
            for s in section.get('subCategories', []):
                temp = []

                if s.get('subCategories'):
                    for sub in s.get('subCategories', []):
                        inner = []
                        for i in sub.get('items', []):
                            k = i.get('itemName', '').strip()
                            v = i.get('value', '').strip()
                            if k:
                                inner.append({"key": k, "value": v})

                        temp.append({
                            "key": sub.get('name', ''),
                            "value": inner
                        })
                else:
                    for i in s.get('items', []):
                        k = i.get('itemName', '').strip()
                        v = i.get('value', '').strip()
                        if k:
                            temp.append({"key": k, "value": v})

                safety.append({
                    "key": s.get('name', ''),
                    "value": temp
                })

        # -------- FEATURES --------
        elif "feature" in name:
            for s in section.get('subCategories', []):
                temp = []

                if s.get('subCategories'):
                    for sub in s.get('subCategories', []):
                        inner = []
                        for i in sub.get('items', []):
                            k = i.get('itemName', '').strip()
                            v = i.get('value', '').strip()
                            if k:
                                inner.append({"key": k, "value": v})

                        temp.append({
                            "key": sub.get('name', ''),
                            "value": inner
                        })
                else:
                    for i in s.get('items', []):
                        k = i.get('itemName', '').strip()
                        v = i.get('value', '').strip()
                        if k:
                            temp.append({"key": k, "value": v})

                features.append({
                    "key": s.get('name', ''),
                    "value": temp
                })

    raw_data = {
        **variant,
        "highlights": highlights,
        "specifications": specifications,
        "safety": safety,
        "features": features
    }

    # ---------------- VALIDATION ----------------
    try:
        validated = CarDetails(**raw_data)

        # convert back to dict for DB
        clean_data = validated.model_dump()

        insert_into_db(clean_data)
        print(f"Valid & Saved: {validated.variant_name}")

    except Exception as e:
        print(f"Validation Error: {variant['variant_url']}")

    

   