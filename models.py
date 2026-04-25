from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Any


# ---------------- KEY-VALUE ----------------
class KeyValue(BaseModel):
    key: str
    value: Any


# ---------------- NESTED SECTION ----------------
class Section(BaseModel):
    key: str
    value: List[Any]


# ---------------- MAIN MODEL ----------------
class CarDetails(BaseModel):
    brand_name: str = Field(..., min_length=1)
    brand_url: HttpUrl
    car_name: str
    car_url: HttpUrl
    variant_name: str
    variant_url: HttpUrl

    highlights: List[str]
    specifications: List[Section]
    safety: List[Section]
    features: List[Section]