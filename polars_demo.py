import polars as pl

df = pl.DataFrame({"name": ["A", "B"], "age": [22, 30]})
print(df)
mean = df.select(pl.col("age").mean())
print(f"mean age={mean['age'][0]}")

