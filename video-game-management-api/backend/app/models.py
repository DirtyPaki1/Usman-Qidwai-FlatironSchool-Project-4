from . import db

# Many-to-many relationship between Game and Platform
game_platform = db.Table('game_platform',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id'), primary_key=True)
)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(50), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'), nullable=False)
    
    # Define relationship to the Developer model
    developer = db.relationship('Developer', backref='games', lazy=True)

    # Define many-to-many relationship with Platform
    platforms = db.relationship('Platform', secondary=game_platform, backref='games', lazy=True)

class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

