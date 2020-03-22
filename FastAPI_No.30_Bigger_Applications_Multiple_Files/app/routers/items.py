from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/" )
async def read_items():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]


@router.get("/{item_id}")
async def read_item(item_id: str):
    return {"name": "Fake Specific Item", "item_id": item_id}
                    # 伪造特定物品

@router.put(
    "/{item_id}",
    tags=["custom"], # custom 习惯
    responses={403: {"description": "Operation forbidden"}}, # 禁止操作
)
async def update_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(status_code=403, detail="You can only update the item: foo")
    return {"item_id": item_id, "name": "The Fighters"}
