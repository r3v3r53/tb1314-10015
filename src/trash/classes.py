from sqlalchemy.dialects.sqlite import BLOB


from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    details = Column(String(500))

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id', onupdate="CASCADE", ondelete="CASCADE"))
    title = Column(String(100))
    details = Column(String(500))
    subject = relationship(Subject)

class Code(Base):
    __tablename__ = 'line'
    id = Column(Integer, primary_key=True)
    value = Column(BLOB)
    type = Column(Enum('LDNK', 'LDNG', name='types'))
    photo_id = Column(Integer, ForeignKey('photo.id', onupdate="CASCADE", ondelete="CASDADE"))
    photo = relationship(Photo)
                        
class Con:
    def __init__(self, db):
        self.db = db
        self.base = Base
        engine = create_engine('sqlite:///%s' % self.db)
        Base.metadata.create_all(engine)
