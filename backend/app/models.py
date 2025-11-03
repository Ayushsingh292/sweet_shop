def to_str_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc
