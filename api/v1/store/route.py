from flask_smorest import Blueprint
from flask.views import MethodView

from api.v1.store.schemas.store_schemas import ItemSchema

blp = Blueprint("Store", __name__, url_prefix="/store", description="TEST DESCRIPTION FOR STORE API")


@blp.route("/")
class Store(MethodView):
    @blp.response(200)
    def get(self):

        return {"msg": "GET"}

    @blp.arguments(ItemSchema)
    @blp.response(201)
    def post(self, item_data: ItemSchema):

        return {"msg": "POST", "item_data": item_data}


@blp.route("/<int:store_id>")
class StoreById(MethodView):
    @blp.response(200)
    def get(self, store_id: int):

        return {"msg": "GET", "store_id": store_id}

    @blp.response(200)
    def put(self, store_id: int):

        return {"msg": "PUT", "store_id": store_id}

    @blp.response(200)
    def patch(self, store_id: int):

        return {"msg": "PATCH", "store_id": store_id}

    @blp.response(204)
    def delete(self, store_id: int):

        return {"msg": "DELETE",  "store_id": store_id}

