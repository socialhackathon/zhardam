from django.utils.translation import ugettext_noop as _

from ..utils import ARTICLE

scenario = {
    'q1': {
        'text': _("Yolo"),
        'answers': {
            'a1': {
                'text': _('Swag'),
                'type': ARTICLE,
                'content': 'https://asjdhalkjdhs.asm/coim/'
            }
        }
    }
}
