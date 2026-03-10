import os
import json
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from dataclasses import dataclass, asdict

#Native Libraries
import constants as c
import functions as f

#Start the window (I have to put it here for dumb reasons.)
root = tk.Tk()

#Load in variables ----------
selected_business_index = 0
filters = ["", "", "", "", "", "", "", ""]

#Load in constants ----------
current_dir = os.path.dirname(os.path.abspath(__file__))

#icon images
filter_image       = ImageTk.PhotoImage(Image.open(c.filter_img).resize((50, 50)))
sort_image         = ImageTk.PhotoImage(Image.open(c.sort_img).resize((50, 50)))
favorite_on_image  = ImageTk.PhotoImage(Image.open(c.favorite_img).resize((50, 50)))
favorite_off_image = ImageTk.PhotoImage(Image.open(c.favorite_outline_img).resize((50, 50)))

#business images
business_images= {
    "generic_business_image" : ImageTk.PhotoImage(Image.open(c.generic_business).resize((500, 400))),
    "fillmore_market" : ImageTk.PhotoImage(Image.open(c.fillmore_market).resize((500, 400))),
    "iceberg" : ImageTk.PhotoImage(Image.open(c.iceberg).resize((500, 400))),
    "kanosh_labs" : ImageTk.PhotoImage(Image.open(c.kanosh_labs).resize((500, 400))),
    "ace_hardware" : ImageTk.PhotoImage(Image.open(c.ace_hardware).resize((500, 400))),
    "mountain_view_mushroom" : ImageTk.PhotoImage(Image.open(c.mountain_view_mushroom).resize((500, 400))),
    "the_flower_mill_and_me" : ImageTk.PhotoImage(Image.open(c.the_flower_mill_and_me).resize((500, 400))),
    "great_lakes_cheese" : ImageTk.PhotoImage(Image.open(c.great_lakes_cheese).resize((500, 400))),
    "ashton_farms_custom_meat" : ImageTk.PhotoImage(Image.open(c.ashton_farms_custom_meat).resize((500, 400))),
    "ifa" : ImageTk.PhotoImage(Image.open(c.ifa).resize((500, 400))),
    "service_drug" : ImageTk.PhotoImage(Image.open(c.service_drug).resize((500, 400))),
    "fillys_carhop_cafe" : ImageTk.PhotoImage(Image.open(c.fillys_carhop_cafe).resize((500, 400))),
    "station_52" : ImageTk.PhotoImage(Image.open(c.station_52).resize((500, 400))),
    "east_millard_swimming_pool" : ImageTk.PhotoImage(Image.open(c.east_millard_swimming_pool).resize((500, 400))),
    "fillmore_city_library" : ImageTk.PhotoImage(Image.open(c.fillmore_city_library).resize((500, 400))),
    "intermountain_health" : ImageTk.PhotoImage(Image.open(c.intermountain_health).resize((500, 400))),
    "revere_health_family_medicine" : ImageTk.PhotoImage(Image.open(c.revere_health_family_medicine).resize((500, 400))),
    "pampered_paws_grooming" : ImageTk.PhotoImage(Image.open(c.pampered_paws_grooming).resize((500, 400))),
    "fillmore_paws_training_center" : ImageTk.PhotoImage(Image.open(c.fillmore_paws_training_center).resize((500, 400))),
    "millard_high_school" : ImageTk.PhotoImage(Image.open(c.millard_high_school).resize((500, 400))),
    "fillmore_elementary_school" : ImageTk.PhotoImage(Image.open(c.fillmore_elementary_school).resize((500, 400))),
    "fillmore_middle_school" : ImageTk.PhotoImage(Image.open(c.fillmore_middle_school).resize((500, 400)))
}

#other images
captcha_image = ImageTk.PhotoImage(Image.open(c.captcha_image).resize((200, 70)))

#Verification functions
# Register the Python function and use a tuple with substitutions for Entry validatecommand
is_rating = root.register(f.is_rating)

#Popup Windows ----------

#Quit the program
def confirmation_window(event=None):
    def quit_program():
        root.destroy()

    pop = tk.Toplevel()

    c.SubTitle(pop, text="Are you sure you want to quit?").grid(row=0, column=0, columnspan=2, sticky="nesw", padx=10, pady=10)
    tk.Button(pop, text="Cancel", command=pop.destroy).grid(row=1, column=0, sticky="nesw", padx=10, pady=10)
    tk.Button(pop, text="Quit", command=quit_program).grid(row=1, column=1, sticky="nesw", padx=10, pady=10)

#Pop up to handle filtering the business list
def filter_window():
    def update_filter_ui(event):
        nonlocal selected_filters
        selected_filters = listbox.curselection()

        #clear the filter ui
        for child in FilterEditor.winfo_children():
            child.destroy()
        
        #read the right filter ui depending on what is selected in the listbox
        if 0 in selected_filters:
            c.SubTitle(FilterEditor, text="Rating").grid(row=0, column=0, padx=10, pady=10)
            
            tk.OptionMenu(FilterEditor, rating_operator, ">", "=", "<").grid(row=0, column=1, padx=10, pady=10)
            tk.Entry(FilterEditor, textvariable=rating_number, validate="key", validatecommand=(is_rating, '%P')).grid(row=0, column=2, padx=10, pady=10)
        else:
            rating_operator.set("=")
            rating_number.set("5.0")
        
        if 1 in selected_filters:
            c.SubTitle(FilterEditor, text="Business open at: ").grid(row=1, column=0, padx=10, pady=10)
            
            tk.OptionMenu(FilterEditor, hour_number, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12").grid(row=1, column=1, padx=10, pady=10)
            tk.OptionMenu(FilterEditor, hour_AmPm, "A.M.", "P.M.").grid(row=1, column=2, padx=10, pady=10)
        else:
            hour_number.set("1")
            hour_AmPm.set("A.M.")

        if 2 in selected_filters:
            c.SubTitle(FilterEditor, text="Favorite").grid(row=2, column=0, padx=10, pady=10)
            c.SubTitle(FilterEditor, text="=").grid(row=2, column=1, padx=10, pady=10)
            
            tk.OptionMenu(FilterEditor, favorite_operator, "True", "False").grid(row=2, column=2, padx=10, pady=10)
        else:
            favorite_operator.set("True")

        if 3 in selected_filters:
            c.SubTitle(FilterEditor, text="Type").grid(row=3, column=0, padx=10, pady=10)
            c.SubTitle(FilterEditor, text="=").grid(row=3, column=1, padx=10, pady=10)
            
            tk.OptionMenu(FilterEditor, type_enumeration, "Food", "Store", "Auto", "Pets", "Agriculture", "Medical", "Recreation", "Education").grid(row=3, column=2, padx=10, pady=10)
        else:
            # clear the type enumeration when the filter is deselected
            type_enumeration.set("")
    
    #Closes the pop window and updates the filtered business selection
    def finish_pop():
        global filters
        if 0 in selected_filters:
            filters[0] = rating_operator.get()
            filters[1] = rating_number.get()
        if 1 in selected_filters:
            filters[2] = hour_number.get()
            filters[3] = hour_AmPm.get()
        if 2 in selected_filters:
            filters[4] = favorite_operator.get()
        if 3 in selected_filters:
            filters[6] = type_enumeration.get()

        filter_businesses()

        pop.destroy()

    def clear_pop():
        global filters
        filters = ["", "", "", "", "", "", "", ""]
        search_var.set("")

        filter_businesses()

        pop.destroy()

    pop = tk.Toplevel()

    #Variables made to be set by the filterEditor UI
    selected_filters = []

    rating_operator = tk.StringVar(pop)
    rating_operator.set("=")
    rating_number = tk.StringVar(pop)
    rating_number.set("5.0")

    hour_number = tk.StringVar(pop)
    hour_number.set("1")
    hour_AmPm = tk.StringVar(pop)
    hour_AmPm.set("A.M.")

    favorite_operator = tk.StringVar(pop)
    favorite_operator.set("True")

    type_enumeration = tk.StringVar(pop)
    type_enumeration.set("Food")

    c.SubTitle(pop, text="Filter").grid(row=0, column=0, padx=10, pady=10)

    listbox = tk.Listbox(pop, selectmode="multiple", exportselection=False)
    listbox.bind("<<ListboxSelect>>", update_filter_ui)
    listbox.grid(row=1, column=0, padx=10, pady=10)

    listbox.insert(tk.END, "Rating")
    listbox.insert(tk.END, "Hours")
    listbox.insert(tk.END, "Favorite")
    listbox.insert(tk.END, "Business Type")

    FilterEditor = tk.Frame(pop)
    FilterEditor.grid(row=2, column=0)

    tk.Button(pop, text="Clear", command=clear_pop).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    tk.Button(pop, text="Done", command=finish_pop).grid(row=3, column=1, sticky="e", padx=10, pady=10)

def sort_window():
    def finish_pop():
        sort_business(sortCategory.get(), sortOrder.get())
        pop.destroy()

    pop = tk.Toplevel()
    sortCategory = tk.StringVar()
    sortCategory.set("Name")
    sortOrder = tk.StringVar()
    sortOrder.set("A-Z (Low to High)")

    c.SubTitle(pop, text="Sort List").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    tk.Label(pop, text="Sort By:").grid(row=1, column=0, padx=10, pady=10)
    tk.OptionMenu(pop, sortCategory, "Name", "Rating", "Favorite", "Business Type").grid(row=2, column=0, padx=10, pady=10)

    tk.Label(pop, text="Sort Order:").grid(row=1, column=1, padx=10, pady=10)
    tk.OptionMenu(pop, sortOrder, "A-Z (Low to High)", "Z-A (High to Low)").grid(row=2, column=1, padx=10, pady=10)

    tk.Button(pop, text="Cancel", command=pop.destroy).grid(row=3, column=0, sticky="e", padx=10, pady=10)
    tk.Button(pop, text="Done", command=finish_pop).grid(row=3, column=1, sticky="e", padx=10, pady=10)

def captcha_window():
    def check_solution(*args):
        if captcha_input.get() == "w3dfs":
            pop.destroy()
            rating_window()
        else:
            captcha_input.set("")
            text.config(text="Please Try Again: ")


    pop = tk.Toplevel()
    captcha_input = tk.StringVar()
    captcha_input.set("") #initialize with something so validation doesn't crash

    c.SubTitle(pop, text="Captcha").grid(row=0, column=0, columnspan = 2, padx=10, pady=10)

    tk.Label(pop, image=captcha_image).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    text = tk.Label(pop, text="Enter the text to continue:")
    text.grid(row=2, column=0, padx=10, pady=10)

    entry = tk.Entry(pop, textvariable=captcha_input)
    entry.grid(row=2, column=1, padx=10, pady=10)
    entry.bind("<Return>", check_solution)
    entry.focus_set()

    tk.Button(pop, text="Cancel", command=pop.destroy).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    tk.Button(pop, text="Submit", command=check_solution).grid(row=3, column=1, padx=10, pady=10, sticky="e")

def rating_window(): #uses the selected_business_index var to leave the right rating
    def finish_pop():
        visible_business_list[selected_business_index].rating = round((visible_business_list[selected_business_index].rating + rating.get()) / 2, 1)
        update_right_list()
        pop.destroy()

    pop = tk.Toplevel()
    rating = tk.DoubleVar()

    c.SubTitle(pop, text="Rating").grid(row=0, column=0, columnspan = 2, padx=10, pady=10)

    tk.Label(pop, text=f"Leave a Rating for {visible_business_list[selected_business_index].name}:").grid(row=1, column=0, padx=10, pady=10)

    tk.Scale(pop, variable=rating, from_=0.0, to=5.0, orient="horizontal").grid(row=1, column=1, padx=10, pady=10)

    tk.Button(pop, text="Cancel", command=pop.destroy).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tk.Button(pop, text="Submit", command=finish_pop).grid(row=2, column=1, padx=10, pady=10, sticky="e")


#Configure UI ----------

#Set up the main window
root.title("Small Business Finder")
root.attributes('-fullscreen', True)
root.grid_rowconfigure(0, weight=1)  # Make row 0 expand vertically
root.grid_columnconfigure(0, weight=1) # Make column 0&1 expand horizontally
root.grid_columnconfigure(1, weight=1) # Make column 0&1 expand horizontally

#Set up Main Screen
left = tk.Frame(root, bg=c.background, relief="ridge", borderwidth=15)
left.grid(row=0, column=0, sticky="nesw")

right = tk.Frame(root, bg=c.background, relief="ridge", borderwidth=15)
right.grid(row=0, column=1, sticky="nesw")

#Populate left frame
c.MainTitle(left, text="Business List:").grid(row=0, column=2, padx=5, pady=5)

filter_btn = tk.Button(left, image=filter_image, command=filter_window)
filter_btn.image = filter_image   # keep a reference to avoid GC
filter_btn.grid(row=1, column=0, padx=5, pady=5)

sort_btn = tk.Button(left, image=sort_image, command=sort_window)
sort_btn.image = sort_image
sort_btn.grid(row=1, column=1, padx=5, pady=5)

# create a StringVar for the search bar (was missing parentheses)
search_var = tk.StringVar()
search_bar = tk.Entry(left, textvariable=search_var, bg=c.entry_background, fg=c.entry_text, font=("Arial", 32))
search_bar.grid(row=1, column=2, columnspan=3, padx=5, pady=5, sticky="ew")

# Scrollable list container
list_container = tk.Frame(left, bg=c.background)
list_container.grid(row=2, column=0, columnspan=5, sticky="nesw", padx=15, pady=15)

# Layout weights for the top row (buttons + search)
left.grid_columnconfigure(0, weight=0)
left.grid_columnconfigure(1, weight=0)
left.grid_columnconfigure(2, weight=1)
left.grid_columnconfigure(3, weight=1)
left.grid_columnconfigure(4, weight=1)

left.grid_rowconfigure(2, weight=1)

canvas = tk.Canvas(list_container, bg=c.background, highlightthickness=0)
scrollBar = tk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollBar.set)

business_display = tk.Frame(canvas, bg=c.background)
business_display.grid_columnconfigure(0, weight=1)

# Keep a reference to the window item so we can keep it in sync with the canvas width
business_display_window = canvas.create_window((0, 0), window=business_display, anchor='nw')

# Keep the embedded frame wide enough when the canvas resizes
def _resize_canvas(event):
    canvas.itemconfigure(business_display_window, width=event.width)

canvas.bind("<Configure>", _resize_canvas)

canvas.grid(row=0, column=0, sticky="nesw")
scrollBar.grid(row=0, column=1, sticky="ns", pady=15)

# Make canvas expand within its container
list_container.grid_rowconfigure(0, weight=1)
list_container.grid_columnconfigure(0, weight=1)

#Functions ----------

def on_business_click(index):
    global selected_business_index
    selected_business_index = index
    update_right_list()

def on_search(*args):
    text = search_var.get()
    global filters
    filters[7] = text
    filter_businesses()

search_var.trace("w", on_search)

def toggle_favorite(idx):
    # Toggle boolean favorite flag
    visible_business_list[idx].favorite = not bool(visible_business_list[idx].favorite)
    update_left_list()

#Empties all children on the left and refills the left side with current businesses and info
def update_left_list():
    for child in business_display.winfo_children():
        child.destroy()
    
    #Iterate through the filtered business list
    for i, business in enumerate(visible_business_list):
        # Create a frame to hold the button content
        btn_frame = tk.Frame(business_display, bg=c.background, relief="solid", borderwidth=1)
        btn_frame.grid(row=i, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        btn_frame.grid_columnconfigure(0, weight=1)
        
        #Create Name button (clickable, takes up space)
        name_btn = tk.Button(
            btn_frame,
            text=f"{business.name} ({business.type})",
            command=lambda idx=i: on_business_click(idx),
            bg=c.background,
            fg="black",
            font=("Arial", 16),
            relief="flat",
            anchor="w",
            padx=10,
            pady=10
        )
        name_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        #Create Favorite button on the right
        if business.favorite:
            favorite_image = favorite_on_image
        else:
            favorite_image = favorite_off_image
        
        fav_btn = tk.Button(
            btn_frame,
            image=favorite_image,
            command=lambda idx=i: toggle_favorite(idx),
            bg=c.background,
            relief="flat",
            padx=5,
            pady=5
        )
        fav_btn.image = favorite_image
        fav_btn.grid(row=0, column=1, sticky="e", padx=5, pady=5)

    if len(visible_business_list) == 0:
        c.Paragraph(business_display, text="No businesses match current settings.").grid(row=0, column=0)

    # Update the scroll region so scrolling matches content size
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def update_right_list():
    #Clear all items in the frame
    for child in right.winfo_children():
        child.destroy()
    
    #figure out which business to display
    try:
        selected_business = visible_business_list[selected_business_index]
    except:
        return None

    #add all the contents according to the selected business
    selected_image = business_images[selected_business.image] 

    c.MainTitle(right, text=f"{selected_business.name} ({selected_business.rating} ★)").grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    tk.Label(right, image=selected_image).grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    c.Paragraph(right, text=selected_business.description, bd=1, relief="ridge").grid(row=2, column=0, padx=5, pady=5, sticky="ew", columnspan=2)
    c.Paragraph(right, text=("Hours: " + selected_business.hours + "\n" + "Address: " + selected_business.address), bd=1, relief="ridge").grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(right, text="Leave a Review", command=captcha_window).grid(row=3, column=1, padx=5, pady=5, sticky="sw")

    right.columnconfigure(0, weight=1)

    
#Switches between fullscreen and window mode. Probs delete this later.
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

#Keybinds ----------

root.bind("<Escape>", confirmation_window) #Sets Escape to quit the program
root.bind("<F11>", toggle_fullscreen) #Sets F11 to toggle fullscreen

#Start and format the business file

#Load the business file into a class ALL CODE BELOW HERE IS UNFINISHED AND UNTESTED PROCEED WITH AT LEAST ONE INSTANCE OF NEVER GONNA GIVE YOU UP ON LOOP IN THE BACKGROUND OR ELSE THE ENTIRE CODE BASE WILL SENSE WEAKNESS AND JUMP YOU IN YOUR BACKALLEY. BE WARNED!

@dataclass
class Business:
    name: str
    rating: float
    image: str
    description: str
    address: str
    hours: str 
    favorite: bool
    type: str

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
            favorite=str(d.get("favorite", "False")).lower() in ("true", "1", "yes"),
            type=str(d.get("type", ""))
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

#Iterate through filter (list of lambda expressions) and only keep business that meet all of them.
def filter_businesses():
    global visible_business_list
    global filters
    
    visible_business_list = business_list.copy() #Has to make it new list so business_list is unchanged

    if filters[0] != "": #first condition isn't empty (rating)
        temp = []
        for business in visible_business_list:
            if filters[0] == ">":   #Greater Than
                if business.rating > float(filters[1]):
                    temp.append(business)
            elif filters[0] == "=": #Equal To
                if business.rating == float(filters[1]):
                    temp.append(business)
            else:                   #Less Than
                if business.rating < float(filters[1]):
                    temp.append(business)

        visible_business_list = temp
    
    if filters[2] != "": #second condition (time)
        filterTime = int(filters[2])
        
        if filters[3] == "P.M." and filterTime != 12:
            filterTime += 12
        elif filters[3] == "A.M." and filterTime == 12:
            filterTime += 12
        
        temp = []
        for business in visible_business_list:
            businessTime = business.hours.split(" ") #load in the business open times, will look like this: ["3", "A.M.", "-", "5", "P.M."]
            businessTime.pop(2)                                               #["3", "A.M.", "5", "P.M."]
            businessTime[0] = int(businessTime[0])
            businessTime[2] = int(businessTime[2])                            #[3, "A.M.", 5, "P.M."]

            if businessTime.pop(1) == "P.M." and businessTime[0] != 12:       #[3, 5, "P.M."]
                businessTime[0] += 12
            if businessTime.pop(2) == "P.M." and businessTime[1] != 12:       #[3, 17]
                businessTime[1] += 12

            #filter the businesses
            if filterTime >= businessTime[0] and filterTime <= businessTime[1]:
                temp.append(business)
        
        visible_business_list = temp
            
    if filters[4] != "": #third condition (favorite)
        temp = []
        for business in visible_business_list:
            if (str(business.favorite) == str(filters[4])):
                temp.append(business)
        visible_business_list = temp
    
    if filters[6] != "": #fourth condition (business type)
        temp = []
        for business in visible_business_list:
            if (business.type == str(filters[6])):
                temp.append(business)
        visible_business_list = temp
    
    if filters[7] != "":
        temp = []
        for business in visible_business_list:
            if (filters[7].lower() in f"{business.name.lower()}, ({business.type.lower()})"):
                temp.append(business)
        visible_business_list = temp
    
    update_left_list()

# sort and update the filtered business list
def sort_business(category, order):
    global visible_business_list
    
    if order == "A-Z (Low to High)":
        is_reverse = False
    else:
        is_reverse = True

    # match the sorting command with the chosen category
    match category:
        case "Name":
            visible_business_list = sorted(visible_business_list, key=lambda business: business.name, reverse=is_reverse)
        case "Rating":
            visible_business_list = sorted(visible_business_list, key=lambda business: business.rating, reverse=is_reverse)
        case "Favorite":
            visible_business_list = sorted(visible_business_list, key=lambda business: business.favorite, reverse=is_reverse)
        case "Business Type":
            visible_business_list = sorted(visible_business_list, key=lambda business: business.type, reverse=is_reverse)
    
    update_left_list()

business_list = load_objects()
visible_business_list = business_list
update_left_list()
update_right_list()

root.mainloop()