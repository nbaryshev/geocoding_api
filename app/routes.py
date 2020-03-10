from app import app, db, form, files, basedir, os, models, logic
import flask


@app.route('/', methods=('GET', 'POST'))
def index():

    upload_form = form.UploadForm()

    if flask.request.method == 'POST':
        if upload_form.validate_on_submit():

            # Uploading new file and add the pass to the database
            new_file = upload_form.upload_new_file()

            new_file_json = logic.convert(new_file.file_path)

        return flask.render_template('results.jin', file_name=new_file.file_name, file_path=new_file.file_path)

    return flask.render_template('index.jin', form=upload_form)
