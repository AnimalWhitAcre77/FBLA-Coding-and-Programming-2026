import os
import json
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from dataclasses import dataclass, asdict

#Native Libraries
import constants as c
import functions as f


@dataclass
class Business:
    name: str
    rating: float
    image: str
    description: str
    address: str
    hours: str 
    favorite: bool

def load_objects() -> list[Business]:
    # Tries to open the json file and coerce fields to the correct types
    def _coerce(d: dict) -> Business:
        return Business(
            name=d.get("name", ""),
            rating=float(d.get("rating", 0.0)),
            image=d.get("image", "generic_business_image"),
            description=d.get("description", ""),
            address=d.get("address", ""),
            hours=d.get("hours", ""),
            favorite=str(d.get("favorite", "False")).lower() in ("true", "1", "yes")
        )

    try:
        with open(Path(__file__).parent / "Businesses.json", "r") as fd:
            return [_coerce(x) for x in json.load(fd)]
    except FileNotFoundError:
        return []

def append_object(object):
    # Turns a business into a dictionary and adds it to the json file.
    data = [asdict(x) for x in load_objects()] + [asdict(object)]
    with open(Path(__file__).parent / "Businesses.json", "w") as fd:
        json.dump(data, fd)

def write_objects(objects) -> list[Business]:
    # Overwrite the JSON file with the provided list of Business objects
    data = [asdict(x) for x in objects]
    with open(Path(__file__).parent / "Businesses.json", "w") as fd:
        json.dump(data, fd)

    return objects

filters = [lambda x: x.favorite == True]

#Iterate through filter (list of lambda expressions) and only keep business that meet all of them.
def filter_businesses():
    filtered_business_list = business_list
    for condition in filters:
        print(condition)
        filtered_business_list = list(filter(condition, filtered_business_list))




filtered_business_list = []
business_list = load_objects()
filter_businesses()
print(filtered_business_list)