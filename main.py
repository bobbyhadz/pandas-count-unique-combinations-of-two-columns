# Pandas: Count the unique combinations of two Columns

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Alice', 'Bobby', 'Alice', 'Alice'],
    'task': ['dev', 'test', 'test', 'dev', 'test', 'dev'],
})

result = df.groupby(['name', 'task']).size().reset_index().rename(
    columns={0: 'count'}
)

print(result)