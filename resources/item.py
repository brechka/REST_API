from flask_restful import Resource, reqparse       # reqparse - for parsing the request
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()           # new object for parsing a request
    parser.add_argument('price',                # parser will look at he JSON payload
                        type=float,
                        required=True,                          # no abble to get request without price
                        help='This field cannot be left blank.'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store id.'
                        )


    @jwt_required()
    # user must provide a valid JWT; work with both Fresh or Non-fresh jwt-token
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found."}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name {} already exists.".format(name)}, 400

        # retrieve data from the request body using the parser
        data = Item.parser.parse_args()
        # create a new item
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted"}
        return {"message": "Item not found."}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']          # price - the only thing is allowed to update
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        # list(map(lambda x: x.json(), ItemModel.query.all()))
        return {"items": [item.json() for item in ItemModel.query.all()]}
