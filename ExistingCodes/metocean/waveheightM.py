from datetime import datetime

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.parser import parse
from matplotlib import style

style.use("ggplot")
link = "http://www.ndbc.noaa.gov/data/realtime2/41046.spec"
dl = pd.read_table(link,delim_whitespace = True,  header=1, parse_dates=[[1,2,3,4]],
                   date_parser=lambda *columns: datetime(2017, *map(int, columns)),)
x = dl.ix[0:,'mo_dy_hr_mn']
y = dl.ix[0:,'m']
box = dict(facecolor='Blue', pad=5, alpha=0.2)
fig = plt.figure()
ax1=fig.add_subplot(111)
ax1.set_title('WaveHeight',bbox=box)
ax1.set_xlabel('DateTime',bbox=box)
ax1.set_ylabel('Height', bbox=box)
#plt.axis([0,24,0.0,7.0])
ax1.plot(x,y,color='r')
plt.savefig('Waveheight',dpi=800)
plt.show()
