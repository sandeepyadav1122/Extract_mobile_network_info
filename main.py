import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import csv
import tkinter as tk
from tkinter import messagebox


def extract_phone_details(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, "US")
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number", None, None, None
        
        # Get the region (location)
        region = geocoder.description_for_number(parsed_number, "en")
        
        # Get the carrier (service provider)
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        # Get the time zone
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        return region, service_provider, time_zones
    
    except phonenumbers.NumberParseException as e:
        return f"Error parsing number: {e}", None, None, None
    except Exception as e:
        return f"Unexpected error: {e}", None, None, None


def save_to_csv(data, filename="phone_details.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def on_submit():
    phone_number = entry.get()
    region, service_provider, time_zones = extract_phone_details(phone_number)
    
    if region.startswith("Error"):
        messagebox.showerror("Error", region)
    else:
        # Display the details in the GUI
        label_region.config(text=f"Region: {region}")
        label_service_provider.config(text=f"Service Provider: {service_provider}")
        label_time_zones.config(text=f"Time Zones: {', '.join(time_zones)}")
        
        # Save to CSV
        save_to_csv([phone_number, region, service_provider, ', '.join(time_zones)])
        messagebox.showinfo("Success", "Details saved to CSV")


# Setting up the GUI
root = tk.Tk()
root.title("Phone Number Details Extractor")

# Input field
tk.Label(root, text="Enter Phone Number with country code :").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, columnspan=2, pady=10)

# Labels to display the results
label_region = tk.Label(root, text="Region: ")
label_region.grid(row=2, columnspan=2, pady=5)

label_service_provider = tk.Label(root, text="Service Provider: ")
label_service_provider.grid(row=3, columnspan=2, pady=5)

label_time_zones = tk.Label(root, text="Time Zones: ")
label_time_zones.grid(row=4, columnspan=2, pady=5)

# Start the GUI event loop
root.mainloop()
