import json

from posemaro.format.util import cast


class Converter:
    def __init__(self, context):
        self._min_ann_id = 1 # index 추가
        self._context = context

        data = {
            'licenses': [],
            'info': {},
            'categories': [],
            'images': [],
            'annotations': []
            }

        data['licenses'].append({
            'name': '',
            'id': 0,
            'url': ''
        })

        data['info'] = {
            'contributor': '',
            'date_created': '',
            'description': '',
            'url': '',
            'version': '',
            'year': ''
        }
        self._data = data

    def is_empty(self):
        return len(self._data['annotations']) == 0

    def _get_image_id(self, item):
        return self._context._get_image_id(item)

    # def has_image(self):
    #     return self.image is not None

    def save_image_info(self, item, filename):
        if item.has_image:
            size = item.image.size
            if size is not None:
                h, w = size
            else:
                h = 0
                w = 0
        else:
            h = 0
            w = 0

        self._data['images'].append({
            'id': self._get_image_id(item),
            'width': int(w),
            'height': int(h),
            'file_name': cast(filename, str, ''),
            'license': 0,
            'flickr_url': '',
            'coco_url': '',
            'date_captured': 0,
        })

    def save_categories(self, dataset):
        raise NotImplementedError()

    def save_annotations(self, item):
        raise NotImplementedError()

    def write(self, path):
        next_id = self._min_ann_id
        for ann in self.annotations:
            if not ann['id']:
                ann['id'] = next_id
                next_id += 1

        with open(path, 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, ensure_ascii=False)

    # @property 데코레이터를 이용하여 get, set ㅁ소드보다 더욱 직관적으로 표현
    @property
    def annotations(self):
        return self._data['annotations']

    @property
    def categories(self):
        return self._data['categories']

    def _get_ann_id(self, annotation):
        ann_id = 0 if self._context._reindex else annotation.id
        if ann_id:
            self._min_ann_id = max(ann_id, self._min_ann_id)
        return ann_id

    # 정적 메소드 : https://wikidocs.net/16074
    @staticmethod
    def _convert_attributes(ann):
        return {k: v for k, v in ann.attributes.items()
                if k not in {'is_crowd', 'score'}
        }