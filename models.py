def create_classes(db):
    class Beach(db.Model):
        __tablename__ = 'beaches'

        id = db.Column(db.Integer, primary_key=True)
        region = db.Column(db.String(64))
        country = db.Column(db.String(64))
        area = db.Column(db.String(64))
        beach_name = db.Column(db.String(64))
        beach_url = db.Column(db.String(64))
        address1 = db.Column(db.String(64))
        address2 = db.Column(db.String(64))
        park_name = db.Column(db.String(64))
        owner_url = db.Column(db.String(64))
        activities = db.Column(db.String(64))
        amenities = db.Column(db.String(64))
        pet_policy = db.Column(db.String(64))
        fees = db.Column(db.String(64))
        phone = db.Column(db.String(64))
        other_names = db.Column(db.String(64))

        def __repr__(self):
            return '<Beach %r>' % (self.beach_name)
    return Beach