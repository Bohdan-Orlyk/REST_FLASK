from flask_smorest import Blueprint, abort
from flask.views import MethodView

from sqlalchemy.exc import SQLAlchemyError

from api.v1.store.models import ItemModel
from db import db

from api.v1.store.schemas.schemas import ItemSchema

blp = Blueprint("Items", __name__, url_prefix="/items", description="TEST DESCRIPTION FOR ITEMS API")


@blp.route("/")
class Items(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):

        return {"msg": "GET"}

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data: ItemSchema) -> ItemSchema:
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occurred while creating the Item")

        return item


@blp.route("/<int:item_id>")
class ItemsById(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id: int) -> ItemSchema:
        item_by_id = ItemModel.query.get_or_404(item_id)

        return item_by_id

    @blp.response(200)
    def put(self, item_id: int):

        return {"msg": "PUT", "store_id": item_id}

    @blp.response(200)
    def patch(self, item_id: int):

        return {"msg": "PATCH", "store_id": item_id}

    @blp.response(204)
    def delete(self, item_id: int):

        return {"msg": "DELETE",  "store_id": item_id}

