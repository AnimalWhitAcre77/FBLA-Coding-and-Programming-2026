#this is a file with a bunch of constants (IDK man)
import os
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk

background = "lightblue"
popup_background = "#F0F0ED"
entry_background = "white"
entry_text = "grey"

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load image robustly (script-relative) and keep a reference to avoid GC (It doesn't actually do this)

#icon images
filter_img = Path(__file__).parent / "Images" / "filter.png"
sort_img = Path(__file__).parent / "Images" / "sort.png"
favorite_img = Path(__file__).parent / "Images" / "favorite.png"
favorite_outline_img = Path(__file__).parent / "Images" / "favorite_outline.png"

#business images
generic_business = Path(__file__).parent / "Images" / "generic_business.jpeg"

#Premade / Formatted widgets ----------

#Label formatted for Main window Titles
class MainTitle(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=background, font=("Arial", 32, "bold"), *args, **kwargs)

#Label formatted for Main window Titles
class SubTitle(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=popup_background, font=("Arial", 16, "bold"), *args, **kwargs)

#Message formatted for paragraph text
class Paragraph(tk.Message):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=background, font=("Arial", 12), *args, **kwargs)

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