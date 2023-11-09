from sqlalchemy.orm import joinedload
from pymysql import IntegrityError
from api.database import db_session
from datetime import datetime

class BaseModel():
    @classmethod
    def with_join(cls, *args):        
        return cls.query.options(list(map(lambda relation: joinedload(relation), args)))

    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def save(self, commit=True):
        self.before_save()
        db_session.add(self)
        if commit:
            try:
                db_session.commit()
            except Exception as e:
                db_session.rollback()
                raise e

        self.after_save()


    def before_update(self, *args, **kwargs):
        if db_session.is_modified(self):
            self.updated_at = datetime.now()

    def after_update(self, *args, **kwargs):
        pass

    def update(self, dict: dict = None, *args, **kwargs):
        if dict:
            for key in dict:
                setattr(self, key, dict[key])

        self.before_update(*args, **kwargs)
        db_session.commit()
        self.after_update(*args, **kwargs)

    def delete(self, commit=True):
        db_session.delete(self)
        if commit:
            db_session.commit()
    
    @classmethod
    def before_bulk_create(cls, iterable, *args, **kwargs):
        pass

    @classmethod
    def after_bulk_create(cls, model_objs, *args, **kwargs):
        pass


    @classmethod
    def bulk_create(cls, iterable, *args, **kwargs):
        cls.before_bulk_create(iterable, *args, **kwargs)
        model_objs = []
        for data in iterable:
            if not isinstance(data, cls):
                data = cls(**data)
            model_objs.append(data)

        db_session.bulk_save_objects(model_objs)
        if kwargs.get('commit', True) is True:
            db_session.commit()
        cls.after_bulk_create(model_objs, *args, **kwargs)
        return model_objs


    @classmethod
    def bulk_create_or_none(cls, iterable, *args, **kwargs):
        try:
            return cls.bulk_create(iterable, *args, **kwargs)
        except IntegrityError as e:
            db_session.rollback()
            return None