from flask_smorest import Blueprint, abort
from flask.views import MethodView

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from api.v1.store.models import StoreModel
from api.v1.store.schemas.schemas import StoreSchema

from db import db

blp = Blueprint("Store", __name__, url_prefix="/store", description="TEST DESCRIPTION FOR STORE API")


@blp.route("/")
class Store(MethodView):
    @blp.response(200)
    def get(self):

        return {"msg": "GET"}

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data: StoreSchema) -> StoreSchema:
        store = StoreSchema(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:  # for unique values (if already exists)
            abort(400, message="Store already exists")
        except SQLAlchemyError:
            abort(500, message="Error occurred while creating the Item")

        return store


@blp.route("/<int:store_id>")
class StoreById(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id: int):
        store = StoreModel.query.get_or_404(store_id)

        return store

    @blp.response(200)
    def put(self, store_id: int):

        return {"msg": "PUT", "store_id": store_id}

    @blp.response(200)
    def patch(self, store_id: int):

        return {"msg": "PATCH", "store_id": store_id}

    @blp.response(204)
    def delete(self, store_id: int):

        return {"msg": "DELETE",  "store_id": store_id}

