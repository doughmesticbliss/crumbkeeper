from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class ProductionAnalytics(Base):
    __tablename__ = "production_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    efficiency_score: Mapped[float] = mapped_column(Float, default=0)


class CapacityAnalytics(Base):
    __tablename__ = "capacity_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    utilization_percent: Mapped[float] = mapped_column(Float, default=0)


class ProductAnalytics(Base):
    __tablename__ = "product_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    product_name: Mapped[str] = mapped_column(String)
    profitability_score: Mapped[float] = mapped_column(Float, default=0)


class EventAnalytics(Base):
    __tablename__ = "event_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    event_name: Mapped[str] = mapped_column(String)
    performance_score: Mapped[float] = mapped_column(Float, default=0)


class WorkloadAnalytics(Base):
    __tablename__ = "workload_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bakery_id: Mapped[int] = mapped_column(index=True)
    strain_score: Mapped[float] = mapped_column(Float, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
