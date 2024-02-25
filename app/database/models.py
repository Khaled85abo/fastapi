from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey, DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class CompanyType(Base):
    __tablename__ = "company_types"
    name:Mapped[str]
    companies: Mapped[list["Company"]] = relationship("Company", back_populates="company_type")

    def __rep__(self):
        return f"<CompanyType={self.name}>"


class Company(Base):
    __tablename__ = "company"
    name: Mapped[str]  = mapped_column(String(100),nullable=False)
    postal_code: Mapped[str]
    email: Mapped[str] = mapped_column(String(1000))
    description: Mapped[str] = mapped_column(Text)
    analytics_module: Mapped[bool] = mapped_column(nullable=True)
    # New
    website : Mapped[str] =mapped_column(nullable = True)
    # Relattions
    company_type: Mapped[CompanyType] = relationship("CompanyType", back_populates= "companies")
    company_type_id: Mapped[int] = mapped_column(ForeignKey("company_types.id", ondelete="SET NULL"), nullable=True)
    def __rep__(self):
        return f"<Company={self.name}>"


class Student(Base):
    __tablename__ = "students"

class Course(Base):
    __tablename__ = "courses"

class Teacher(Base):
    __tablename__ = "teachers"

class Classroom(Base):
    __tablename__="classrooms"

class Supervisor(Base):
    __tablename__ = "Supervisors"

class MeetingRoom(Base):
    __tablename__  = "meetingroom"
