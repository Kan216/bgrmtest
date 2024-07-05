import requests
import tkinter as tk
from tkinter import messagebox

# Define the function to fetch and display the data
def fetch_data():
    url = "https://covid.cdc.gov/covid-data-tracker/#maps_percent-covid-deaths"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        global_data = data['totals']
        
        total_vaccinations = global_data['total_vaccine_doses_administered']
        total_people_vaccinated = global_data['total_vaccine_persons_vaccinated']
        total_people_fully_vaccinated = global_data['total_vaccine_persons_fully_vaccinated']
        
        # Create a new window to display the data
        result_window = tk.Toplevel(root)
        result_window.title("Global COVID-19 Vaccination Data")
        
        tk.Label(result_window, text="Global COVID-19 Vaccination Data", font=('Helvetica', 16, 'bold')).pack(pady=10)
        tk.Label(result_window, text=f"Total Vaccinations: {total_vaccinations}").pack(pady=5)
        tk.Label(result_window, text=f"Total People Vaccinated: {total_people_vaccinated}").pack(pady=5)
        tk.Label(result_window, text=f"Total People Fully Vaccinated: {total_people_fully_vaccinated}").pack(pady=5)
    else:
        messagebox.showerror("Error", f"Failed to fetch data from the API. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("COVID-19 Data Fetcher")

# Create a button to fetch the data
fetch_button = tk.Button(root, text="Fetch Global COVID-19 Data", command=fetch_data)
fetch_button.pack(pady=20)

# Start the main event loop
root.mainloop()
