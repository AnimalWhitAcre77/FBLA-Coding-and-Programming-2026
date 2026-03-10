#this is a file with a bunch of constants (IDK man)
import os
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk

background = "lightblue"
popup_background = "#F0F0ED"
entry_background = "white"
entry_text = "gray7"

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load image robustly (script-relative) and keep a reference to avoid GC (It doesn't actually do this)

#icon images
filter_img = Path(__file__).parent / "Images" / "filter.png"
sort_img = Path(__file__).parent / "Images" / "sort.png"
favorite_img = Path(__file__).parent / "Images" / "favorite.png"
favorite_outline_img = Path(__file__).parent / "Images" / "favorite_outline.png"

#business images
generic_business = Path(__file__).parent / "Images" / "generic_business.jpeg"
fillmore_market = Path(__file__).parent / "Images" / "fillmore_market.jpg"
iceberg = Path(__file__).parent / "Images" / "iceberg.jpeg"
kanosh_labs = Path(__file__).parent / "Images" / "kanosh_labs.jpeg"
ace_hardware = Path(__file__).parent / "Images" / "ace_hardware.jpeg"
mountain_view_mushroom = Path(__file__).parent / "Images" / "mountain_view_mushroom.jpeg"
the_flower_mill_and_me = Path(__file__).parent / "Images" / "the_flower_mill_and_me.jpeg"
great_lakes_cheese = Path(__file__).parent / "Images" / "great_lakes_cheese.jpeg"
ashton_farms_custom_meat = Path(__file__).parent / "Images" / "ashton_farms_custom_meat.jpeg"
ifa = Path(__file__).parent / "Images" / "ifa.jpeg"
service_drug = Path(__file__).parent / "Images" / "service_drug.jpeg"
fillys_carhop_cafe = Path(__file__).parent / "Images" / "fillys_carhop_cafe.jpeg"
station_52 = Path(__file__).parent / "Images" / "station_52.jpeg"
east_millard_swimming_pool = Path(__file__).parent / "Images" / "east_millard_swimming_pool.jpeg"
fillmore_city_library = Path(__file__).parent / "Images" / "fillmore_city_library.jpeg"
intermountain_health = Path(__file__).parent / "Images" / "intermountain_health.jpeg"
revere_health_family_medicine = Path(__file__).parent / "Images" / "revere_health_family_medicine.jpeg"
pampered_paws_grooming = Path(__file__).parent / "Images" / "pampered_paws_grooming.jpeg"
fillmore_paws_training_center = Path(__file__).parent / "Images" / "fillmore_paws_training_center.png"
millard_high_school = Path(__file__).parent / "Images" / "millard_high_school.jpeg"
fillmore_elementary_school = Path(__file__).parent / "Images" / "fillmore_elementary_school.jpeg"
fillmore_middle_school = Path(__file__).parent / "Images" / "fillmore_middle_school.jpeg"

captcha_image = Path(__file__).parent / "Images" / "captcha_text.png"

#Premade / Formatted widgets ----------

#Label formatted for Main window Titles
class MainTitle(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=background, font=("Arial", 32, "bold"), *args, **kwargs)

#Label formatted for pop up windows
class SubTitle(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=popup_background, font=("Arial", 16, "bold"), *args, **kwargs)

#Message formatted for paragraph text
class Paragraph(tk.Message):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=background, font=("Arial", 16), *args, **kwargs)

#Frame configured to activate the specified command with the specidied id when clicked
class ClickableFrame(tk.Frame):
    def __init__(self, parent, frame_id, on_click=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.frame_id = frame_id
        self.on_click = on_click
    
        # Bind click event to this frame and all children
        self.bind("<Button-1>", self._on_click)
        self.bind_all("<Button-1>", self._on_click)  # catches clicks on child widgets too
    
    def _on_click(self, event):
        #Only trigger if the click is on the frame or its children
        if event.widget == self or self.winfo_children() and event.widget in self.winfo_children():
            if self.on_click:
                self.on_click(self.frame_id)