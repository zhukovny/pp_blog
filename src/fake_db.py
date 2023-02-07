import dataclasses
from typing import Dict


@dataclasses.dataclass(frozen=True)
class Item:
    id: int
    name: str

    @staticmethod
    def from_json(json: Dict) -> "Item":
        return Item(
            id=json["id"],
            name=json["name"],
        )


fake_items_db = [
    Item.from_json({"id": 0, "name": "Foo"}),
    Item.from_json({"id": 1, "name": "Bar"}),
    Item.from_json({"id": 2, "name": "Baz"}),
]
