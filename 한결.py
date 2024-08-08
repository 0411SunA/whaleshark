# google sheet pandas로 읽어오는 방법

import pandas as pd

# https://docs.google.com/spreadsheets/d/1McH-oBzPZ8ewfyEl605wq-9b3gZHCIIBVbWHEHwNnIs/edit?gid=941998772#gid=941998772
gsheet_url = "https://docs.google.com/spreadsheets/d/1McH-oBzPZ8ewfyEl605wq-9b3gZHCIIBVbWHEHwNnIs/gviz/tq?tqx=out:csv&sheet=ames-spot"

df = pd.read_csv(gsheet_url)
df
