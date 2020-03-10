import flask_wtf
import os
import wtforms

from app import files, basedir, models


class UploadForm(flask_wtf.FlaskForm):
    file = wtforms.FileField('File: ')
    submit = wtforms.SubmitField('Upload')

    def upload_new_file(self):

        # Retrieve name of the file from UploadForm and save
        filename = files.save(self.file.data)

        # Retrieve a path to the file
        directory = 'static/files/' + filename
        file_path = os.path.join(basedir, directory)

        # Sending data to the model
        new_file = models.File.upload_file(file_path=file_path, file_name=filename)

        return new_file


