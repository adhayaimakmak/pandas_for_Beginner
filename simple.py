import pandas as pd
import random as rd
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  # เพิ่มบรรทัดนี้

data = pd.DataFrame({
    'date': [datetime.date(2023, 1, 1) + datetime.timedelta(days=i) for i in range(10)],
    'value': [rd.randint(1, 100) for _ in range(10)]
})

ax = data.plot(x='date', y='value', kind='line', color='black', legend=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.grid(False)
ax.set_title('')
ax.set_xlabel('')
ax.set_ylabel('')

plt.tight_layout()
plt.show()