import requests
import numpy as np
import matplotlib.pyplot as plt
from weasyprint import HTML
from datetime import datetime

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

res = requests.get(url)

data = res.json()

info = data['data']
years = []
pop = []

for entry in info:
    years.append(entry['Year'])
    pop.append(entry['Population'])

years.reverse()
pop.reverse()

b = np.array(pop) / 1000000
max_pop = b[len(b) -1 ]
min_pop = b[0]

print(max_pop)

plt.figure()
plt.scatter(years, b)
plt.plot(years, b, label='População', linestyle='--')
plt.xlabel('Anos')
plt.ylabel('População (Milhões)')
plt.grid()
plt.title("População EUA Plot")
plt.legend()
plt.savefig('PopulationPlot.png')

plt.figure()
plt.bar(years, b, label='População')
plt.xlabel('Anos')
plt.ylabel('População (Milhões)')
plt.ylim(min_pop-10, max_pop + 10)
plt.grid()
plt.title("População EUA Bars")
plt.legend()
plt.savefig('PopulationBars.png')

plt.figure()
plt.scatter(years, b, label='População')
plt.xlabel('Anos')
plt.ylabel('População (Milhões)')
plt.ylim(min_pop-10, max_pop + 10)
plt.grid()
plt.title("População EUA Bars")
plt.legend()
plt.savefig('PopulationScatter.png')

plt.show()             

date = datetime.now()

formatted_time = date.strftime("%d/%m/%Y %H:%M")

with open('eua.html', 'r') as f:
    html_script = f.read()
    f.close()


new_html = html_script.replace('**Date**', str(formatted_time))
new_html = new_html.replace('**EuaGraphPlot**', 'PopulationPlot.png')
new_html = new_html.replace('**EUAGraphBars**','PopulationBars.png')
new_html = new_html.replace('**EUAGraphScatter**','PopulationScatter.png')

with open('eua2.html', 'wt') as new_file:
    new_file.write(new_html)
    new_file.close()


htmldoc = HTML('eua2.html')
htmldoc.write_pdf('eua.pdf')
