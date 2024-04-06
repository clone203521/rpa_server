from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AccessRecord(db.Model):
    __tablename__ = 'access_record'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100), nullable=False)
    access_date = db.Column(db.Date, nullable=False)
    count = db.Column(db.Integer, default=1)

    def __repr__(self):
        return (f"<AccessRecord(id={self.id}, ip_address={self.ip_address}, "
                f"access_date={self.access_date}, count={self.count})>")


class Browser(db.Model):
    __tablename__ = 'browser'
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer, nullable=False)
    browser_name = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(50))
    remarks = db.Column(db.Text)
    label = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(100))
