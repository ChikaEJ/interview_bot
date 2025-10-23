from typing import Generic, Type, Optional, Any

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from db.schemas.generics import CreateSchemaType, ModelType, ReadSchemaType


class BaseCRUD(Generic[ModelType, CreateSchemaType, ReadSchemaType]):


    def __init__(self, model: Type[ModelType], read_schema: Type[ReadSchemaType]):
        self.model = model
        self.read_schema = read_schema

    async def create(
        self, session: AsyncSession, obj_in: CreateSchemaType
    ) -> ReadSchemaType:
        obj = self.model(**obj_in.model_dump())
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return self.read_schema.model_validate(obj)

    async def get(
        self, session: AsyncSession, obj_id: Any
    ) -> Optional[ReadSchemaType]:
        result = await session.execute(select(self.model).where(self.model.id == obj_id))
        obj = result.scalar_one_or_none()
        return self.read_schema.model_validate(obj) if obj else None

    async def get_all(
        self, session: AsyncSession, limit: int = 100, offset: int = 0
    ) -> list[ReadSchemaType]:
        result = await session.execute(select(self.model).limit(limit).offset(offset))
        objs = result.scalars().all()
        return [self.read_schema.model_validate(o) for o in objs]

    async def update(
        self, session: AsyncSession, obj_id: Any, obj_in: dict | CreateSchemaType
    ) -> Optional[ReadSchemaType]:
        if isinstance(obj_in, BaseModel):
            data = obj_in.model_dump(exclude_unset=True)
        else:
            data = obj_in

        stmt = (
            update(self.model)
            .where(self.model.id == obj_id)
            .values(**data)
            .returning(self.model)
        )
        result = await session.execute(stmt)
        await session.commit()
        obj = result.scalar_one_or_none()
        return self.read_schema.model_validate(obj) if obj else None

    async def delete(self, session: AsyncSession, obj_id: Any) -> bool:
        stmt = delete(self.model).where(self.model.id == obj_id)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount > 0

    async def filter_by(self, session: AsyncSession, **kwargs) -> list[ReadSchemaType]:
        stmt = select(self.model).filter_by(**kwargs)
        result = await session.execute(stmt)
        objs = result.scalars().all()
        return [self.read_schema.model_validate(o) for o in objs]