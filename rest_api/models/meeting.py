from typing import Optional, List
from rest_api.db import db


class MeetingModel(db.Model):
    """ SQLAlchemy DB Model for Meeting """

    __tablename__ = 'meetings'

    meeting_date = db.Column(db.String(10), primary_key=True)
    theme = db.Column(db.String(50))
    pbj_topic = db.Column(db.String(50), nullable=True)
    right_brain_topic = db.Column(db.String(50), nullable=True)
    pro_talk_topic = db.Column(db.String(50), nullable=True)

    def __init__(self,
                 meeting_date: str,
                 theme: str,
                 pbj_topic: Optional[str] = None,
                 right_brain_topic: Optional[str] = None,
                 pro_talk_topic: Optional[str] = None) -> None:
        self.meeting_date = meeting_date
        self.theme = theme
        self.pbj_topic = pbj_topic
        self.right_brain_topic = right_brain_topic
        self.pro_talk_topic = pro_talk_topic

    @classmethod
    def meeting_by_date(cls, meeting_date: str) -> Optional['MeetingModel']:
        return cls.query.filter_by(meeting_date=meeting_date).first()

    @classmethod
    def all_meetings(cls) -> List['MeetingModel']:
        return cls.query.all()

    def as_dict(self) -> dict:
        return {'meeting_date': self.meeting_date,
                'theme': self.theme,
                'pbj_topic': self.pbj_topic,
                'right_brain_topic': self.right_brain_topic,
                'pro_talk_topic': self.pro_talk_topic}

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
