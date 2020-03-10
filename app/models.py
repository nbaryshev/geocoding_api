from app import db, files, os, form


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String)
    file_name = db.Column(db.String)

    @classmethod
    def upload_file(cls, file_path=None, file_name=None):
        new_file = File(file_path=file_path, file_name=file_name)

        db.session.add(new_file)
        db.session.commit()

        return new_file

    def upload_get_filepath(self):
        file