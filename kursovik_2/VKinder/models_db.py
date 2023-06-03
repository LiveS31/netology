import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """Table model 'user'."""
    __tablename__ = 'user'
    id_user = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)


class FavoritesProfile(Base):
    """Table model 'favorites_profile'"""
    __tablename__ = 'favorites_profile'
    id_favorites_profile = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    city = sq.Column(sq.String)
    link = sq.Column(sq.String)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user.id_user', ondelete='CASCADE'))


class BlackProfile(Base):
    """Table model 'black_profile'"""
    __tablename__ = 'black_profile'
    id_black_profile = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    city = sq.Column(sq.String)
    link = sq.Column(sq.String)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user.id_user', ondelete='CASCADE'))


class Photos(Base):
    """Table model 'photos'."""
    __tablename__ = 'photos'
    id_photos = sq.Column(sq.Integer, primary_key=True)
    link_foto = sq.Column(sq.String)
    count_likes = sq.Column(sq.Integer)
    id_favorites_profile = sq.Column(sq.Integer, sq.ForeignKey('favorites_profile.id_favorites_profile',
                                                               ondelete='CASCADE'))


def create_tables(engine):
    """Сreates database tables."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
