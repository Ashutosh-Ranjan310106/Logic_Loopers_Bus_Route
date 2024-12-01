import csv

# Define the input and output file names
input_file = "st.txt"
csv_file = "stops.csv"

# Read data from the text file
stops_data = []
with open(input_file, "r") as file:
    for line in file:
        # Strip any extra whitespace or newline characters
        line = line.strip()
        # Split line on colon to get stop_name and location_cordinate
        if ':' in line:
            stop_name, location_cordinate = line.split(":", 1)
            location_cordinate = location_cordinate.strip()  # Ensure no extra whitespace
        else:
            stop_name = line
            # Skip lines that are not valid stop names
            if stop_name == "Back to top" or len(stop_name) <= 2:
                continue
            location_cordinate = ""
        
        stops_data.append({"stop_name": stop_name, "location_cordinate": location_cordinate})

# Write data to CSV
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["stop_name", "location_cordinate"])
    
    # Write data rows
    for stop in stops_data:
        writer.writerow([stop["stop_name"], stop["location_cordinate"]])

print(f"Data successfully written to {csv_file}")
