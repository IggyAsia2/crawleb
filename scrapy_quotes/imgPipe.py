from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import hashlib
import scrapy

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        # Customize file path (optional)
        image_guid = hashlib.sha1(request.url.encode()).hexdigest() 
        return f'full/{image_guid}.jpg' 

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Image Download Failed")
        item['image_paths'] = image_paths
        return item