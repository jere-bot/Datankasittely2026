import pandas as pd

def get_shape(df):
    return df.shape

def first_two(df):
    return df.head(2)

def last_two(df):
    return df.tail(2)

def analyze_data(users):
    df = pd.DataFrame(users)

    shape = get_shape(df)
    first = first_two(df)
    last = last_two(df)

    return {"shape": shape, "first": first, "last": last}