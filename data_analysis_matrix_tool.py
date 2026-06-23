import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

plt.imshow([data["Marks"]], aspect="auto")
plt.colorbar()

plt.title("Heatmap of Student Marks")

plt.show()
