# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
df = pd. read_csv("avocado.csv")


# %%
df


# %%
df.head(3)


# %%
df.head(3)


# %%
df.head(3)


# %%
albany_df = df[df["region"]=="Albany"]
albany_df.head()


# %%
albany_df.index


# %%
albany_df.set_index("Date")


# %%
albany_df.head()


# %%
albany_df = albany_df.set_index("Date")


# %%
albany_df.head()


# %%
#albany_df.set_index("Date", inplace = True)


# %%
albany_df['AveragePrice'].plot()


# %%


