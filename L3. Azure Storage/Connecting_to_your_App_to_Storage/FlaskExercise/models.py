from FlaskExercise import app, db
from flask import flash
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import uuid

blob_container = app.config['images']
storage_url = "https://{}.blob.core.windows.net/".format(app.config['helloworld12345'])
blob_service = BlobServiceClient(account_url=storage_url, credential=app.config['/6sf0QPfSsI/Ml3dfudx6sjQGFAKIawLZWW4JTgBFYBlaEcLVvzls73JROgsn/QOW54frnWRQWz7+AStWH2VMA=='])

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    scientific_name = db.Column(db.String(75))
    description = db.Column(db.String(800))
    image_path = db.Column(db.String(100))

    def __repr__(self):
        return '<Animal {}>'.format(self.body)

    def save_changes(self, file):
        if file:
            filename = secure_filename(file.filename)
            fileExtension = filename.rsplit('.', 1)[1]
            randomFilename = str(uuid.uuid1())
            filename = randomFilename + '.' + fileExtension
            try:
                blob_client = blob_service.get_blob_client(container=blob_container, blob=filename)
blob_client.upload_blob(file)
                pass
                if self.image_path:
                    blob_client = blob_service.get_blob_client(container=blob_container, blob=self.image_path)
blob_client.delete_blob()
                    pass
            except Exception as err:
                flash(err)
            self.image_path = filename
        db.session.commit()
