from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(64))

    def readyToJSON(self, keys):
        """
        Params:
            keys [Iterable[str]]
        """
        d = {}
        for k in keys:
            v = getattr(self, k)
            d[k] = v
        return d

    def __repr__(self):
        return '<Student %r>' % self.id
