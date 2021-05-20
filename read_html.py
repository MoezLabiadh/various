# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:08:13 2020

@author: MLABIADH
"""

import pandas as pd
import requests

url = 'https://apps.nrs.gov.bc.ca/ext/soss/'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

dfs = dfs = pd.read_html(r.text)