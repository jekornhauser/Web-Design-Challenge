import pandas as pd
from IPython.display import HTML 

a = pd.read_csv(r"C:\Users\jekor\Desktop\Web-Design-Challenge\Resources\cities.csv")
result = a.to_html()
text_file = open(r"data.html", "w")
text_file.write(result)
text_file.close()
print("Done")