from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.parser import parse
from matplotlib import style

style.use("ggplot")
link = "http://www.ndbc.noaa.gov/data/realtime2/51211.adcp"
dl = pd.read_table(link,delim_whitespace = True,  header=1, parse_dates=[[1,2,3,4]],
                   date_parser=lambda *columns: datetime(2017, *map(int, columns)),)
x = dl.ix[0:,'mo_dy_hr_mn']
y = dl.ix[0:,'cm/s']
box = dict(facecolor='Blue', pad=5, alpha=0.2)
fig = plt.figure()
ax1=fig.add_subplot(111)
ax1.set_title('ADCP',bbox=box)
ax1.set_xlabel('DateTime',bbox=box)
ax1.set_ylabel('Current', bbox=box)
#plt.axis([0,24,0.0,12.0])
ax1.plot(x,y,color='b')
plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.savefig('ADCP',dpi=800)
plt.show()
