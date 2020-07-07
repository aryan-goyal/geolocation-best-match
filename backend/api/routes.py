import os
from flask import Flask, flash, request, redirect, url_for, json
from werkzeug import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

UPLOAD_FOLDER = '/path/to/the/uploadRawCSV'
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/xml/<filename>', methods=['GET'])
def get_xml():
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/upload_options', methods=['POST'])
def set_options():
    file = request.files['file']
    myfile = file.read()
    jsonify(files)
    return redirect(url_for('uploaded_file',
                            filename=filename))


@app.route('/upload_csv', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))


if __name__ == '__main__':
    app.run(debug=False)
