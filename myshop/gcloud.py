from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin

class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    """
    Google file storage class which gives a media file path for DEDIA_URL not google generated one
    """ 
    def __init__(self, *args, **kwargs):
            if not settings.MEDIA_URL:
                raise Exception('MEDIA_URL has not been configured')
            kwargs['bucket_name'] = setting('GS_BUCKET_NAME', strict=True)
            super(GoogleCloudMediaFileStorage, self).__init__(*args, **kwargs)
    
    bucket_name = settings("GS_BUCKET_NAME")
    
    def url(self,name):
        """
        GIves correct MEDIA_URL and not google generated url.
        """
        return urljoin(settings.MEDIA_URL,name)
