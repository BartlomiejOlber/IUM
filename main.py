import pandas as pd

MAX_PRICE = 100000


def clean_products():
    products = pd.read_json("data/products.jsonl", lines=True)
    products.loc[products["price"] < 0, "price"] *= -1
    products = products[products["price"] < MAX_PRICE]
    products["category_path"] = products["category_path"].str.rsplit(';', n=1, expand=True)[1]
    products.rename(columns={"category_path": "category"}, inplace=True)
    products.to_json("data/products_clean.jsonl", orient='records', lines=True)
    return products


def clean_sessions():
    sessions = pd.read_json("data/sessions.jsonl", lines=True)
    products = pd.read_json("data/products_clean.jsonl", lines=True)
    print(sessions.shape[0])
    sessions = sessions[sessions["product_id"].isin(products["product_id"])]
    sessions = sessions.fillna({"user_id": sessions.groupby("session_id")["user_id"].transform('min')})
    sessions = sessions.dropna(subset=["user_id"])
    print(sessions.shape[0])
    sessions = sessions.astype({'user_id': 'int32', 'product_id': 'int32', 'purchase_id': "Int64"}, errors='ignore')
    sessions.to_json("data/sessions_clean.jsonl", orient='records', lines=True)
    return sessions


def foo(sessions: pd.DataFrame, users: pd.DataFrame):
    bought = sessions[sessions["event_type"] == "BUY_PRODUCT"]
    views = sessions[sessions["event_type"] == "VIEW_PRODUCT"]
    successful_sessions = sessions[sessions["session_id"].isin(bought["session_id"])]
    successful_views_count = successful_sessions.groupby("session_id")["user_id"].agg('count') - 1
    print(successful_views_count.values)
    import matplotlib.pyplot as plt
    plt.figure()
    _ = plt.hist(successful_views_count.values)
    plt.show()

    bought_with_discount = bought[bought["offered_discount"] != 0]
    successful_sessions_with_discount = sessions[sessions["session_id"].isin(bought_with_discount["session_id"])]
    successful_views_count_with_discount = successful_sessions_with_discount.groupby("session_id")["user_id"].agg('count') - 1
    plt.figure()
    _ = plt.hist(successful_views_count_with_discount.values)
    plt.show()
    print(bought_with_discount.shape[0])
    print(bought.shape[0])

if __name__ == '__main__':
    # clean_products()
    foo(pd.read_json("data/sessions_clean.jsonl", lines=True), pd.read_json("data/users.jsonl", lines=True))




