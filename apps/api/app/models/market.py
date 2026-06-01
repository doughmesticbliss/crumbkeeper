from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class MarketEvent(Base):
    __tablename__ = "market_events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(String)
    event_date: Mapped[str] = mapped_column(String)


class MarketInventoryPlan(Base):
    __tablename__ = "market_inventory_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    projected_units: Mapped[int] = mapped_column(default=0)


class EventForecast(Base):
    __tablename__ = "event_forecasts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    projected_sales: Mapped[float] = mapped_column(Float, default=0)


class SellThroughRecord(Base):
    __tablename__ = "sell_through_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    sell_through_percent: Mapped[float] = mapped_column(Float, default=0)


class PackagingPlan(Base):
    __tablename__ = "packaging_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    label_count: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
