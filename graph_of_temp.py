import matplotlib.pyplot as plt
import json

# This code will read the json file and make a varyable called data for the program to use
with open("phoenix_temp.json", "r") as temp_file:
    data = json.load(temp_file)

"""
    The following code will take the data that was gotten from the json file
    and will define what the axes will show. For the x-axis it will only be the
    year that the pemperatures are. For the y-axis it will be both the high and
    the low temperatures.
"""
year_x = [year["year"] for year in data]
temp_y_high = [temp["temp_h"] for temp in data]
temp_y_low = [temp["temp_l"] for temp in data]

"""
    The code here will make the graph visible, with plt.figure making the dimentions of the
    graph, and the two plt.bar functions making the bar of the actual temperatures.
"""
plt.figure(figsize=(15, 8))
plt.bar(year_x, temp_y_high, color="orange", width=0.9, edgecolor="gray")
plt.bar(year_x, temp_y_low, color="blue", width=0.9, edgecolor="black")

"""
    The code below defines what the graph needs to look like, things like the title of the 
    graph, the labels for the axes, how much to rotate the tick mark label, where to start 
    showing the data and where to stop, and the legend of the graph.
"""
plt.title("Temperatures On The 4th Of July In Phoenix, AZ")
plt.xlabel("Year")
plt.ylabel("Temperature (F)")
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.ylim(70, 120)
plt.legend(["High Temp: Orange", "Low Temp: Blue"])

# This is the final command that tells the program to display the graph in a window
plt.show()