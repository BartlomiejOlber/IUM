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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # clean_products()
    clean_sessions()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
