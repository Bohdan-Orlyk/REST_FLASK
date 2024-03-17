from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "item_1",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores": stores}