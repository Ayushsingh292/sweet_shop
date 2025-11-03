from mongoengine import Document, StringField, FloatField, IntField

class Sweet(Document):
    name = StringField(required=True)
    category = StringField(required=True)
    price = FloatField(required=True)
    quantity = IntField(default=0)
