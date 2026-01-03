import pandas as pd


def clean_features(df, use_month_feature, t_imputation_value, test=False):
    rain_cols = ["precipitation_inch", "snow_inch", "snow_depth_inch"]
    df = df.copy()
    df.columns = ["date", "max_temp_F", "min_temp_F", "precipitation_inch", "snow_inch", "snow_depth_inch"]
    df["date"] = pd.to_datetime(df["date"])
    if test:  # test_df
        all_dates = pd.date_range(start=df["date"].min(), end=df["date"].max() + pd.Timedelta(days=1), freq="D")
        df = df.set_index("date").reindex(all_dates).reset_index().rename(columns={"index": "date"})

    if use_month_feature:
        df["month"] = (df["date"].dt.dayofyear - 1) / 365 * 12

    for col in rain_cols:
        for i in range(len(df)):
            if df[col].iloc[i] == "T":
                df.loc[i, col] = t_imputation_value
        df[col] = df[col].astype(float)

    return df


def train_val_split(full_train_df, val_size):
    val_size_days = int(len(full_train_df) * val_size)
    train_df = full_train_df.iloc[:-val_size_days].copy()
    val_df = full_train_df.tail(val_size_days).copy()
    print(f"Train set interval: {train_df['date'].min().date()} to {train_df['date'].max().date()}")
    print(f"Validation set interval: {val_df['date'].min().date()} to {val_df['date'].max().date()}")
    return train_df, val_df
