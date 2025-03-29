# "variants of type: null", "boolean", "object", "array", "number", "integer", "string"
ITEMS_SCHEMA = {
    "type": "object",
    "properties":{
        "Items": {
            "type": "array",
            "properties":{
                "id": {"type": "number"},
                "desc": {"type": "string"},
                "price": {"type": "number"},
                "title": {"type": "string"},
                "img": {"type": "string"},
                },
                "required":["id", "title", "price", "desc", "img"]},
        "LastEvaluatedKey": {"type": "object"},
    },
    "required":["Items", "LastEvaluatedKey"],
}