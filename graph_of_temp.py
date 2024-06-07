import matplotlib.pyplot as plt
import json

with open("phoenix_temp.json", "r") as temp_file:
    data = json.load(temp_file)

year_x = [year["year"] for year in data]
temp_y = [temp["temp"] for temp in data]

plt.figure(figsize=(15, 8))
plt.bar(year_x, temp_y, color="black")

plt.title("Temperatures On The 4th Of July In Phoenix, AZ")
plt.xlabel("Year")
plt.ylabel("Temperature (F)")
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.ylim(90, 120)

plt.show()