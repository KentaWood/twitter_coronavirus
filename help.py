# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Data
data = {"LK": 1, "RU": 1, "CA": 3, "TW": 3,"UZ": 3, "US": 4, "CN": 4, "ES": 5,"HK": 6, "KR": 284}
# Plotting each data point individually
for country, count in data.items():
    print(country)
    print(count)
    plt.bar(country,count)

plt.xlabel('Countries')
plt.ylabel('Counts')
plt.savefig('#코로나바이러스.country.png')
plt.close()

