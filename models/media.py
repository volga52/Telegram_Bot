from sqlalchemy import Column, Integer, String

from data_base.dbcore import Base


class MediaIds(Base):
    __tablename__ = 'Media_ids'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    filename = Column(String(255))
