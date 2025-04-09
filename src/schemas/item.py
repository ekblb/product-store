# "variants of type: null", "boolean", "object", "array", "number", "integer", "string"
ITEMS_SCHEMA = {
    "type": "object",
    "properties":{
        "Items": {
            "type": "array",
            "properties":{
                "id": {"type": "number"},
                "cat": {"type": "string"},
                "desc": {"type": "string"},
                "price": {"type": "number"},
                "title": {"type": "string"},
                "img": {"type": "string"},
                },
                "required":["id", "cat", "title", "price", "desc", "img"]},
        "LastEvaluatedKey": {"type": "object"},
    },
    "required":["Items", "LastEvaluatedKey"],
}