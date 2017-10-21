from django.utils.translation import ugettext_noop as _

from ..utils import ARTICLE, QUESTION

scenario = {
    'q1': {
        'text': _("Demo?"),
        'answers': {
            'a1': {
                'text': _('Debug it'),
                'type': QUESTION,
                'content': 'q2',
            },
            'a2': {
                'text': _('Debug it 2'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            },
            'a3': {
                'text': _('Debug it 3'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            }
        }
    },
    'q2': {
        'text': _("Demo?"),
        'answers': {
            'a1': {
                'text': _('Debug it'),
                'type': QUESTION,
                'content': 'q3',
            },
            'a2': {
                'text': _('Debug it 2'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            },
            'a3': {
                'text': _('Debug it 3'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            }
        }
    },
    'q3': {
        'text': _("Demo?"),
        'answers': {
            'a2': {
                'text': _('Debug it 2'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            },
            'a3': {
                'text': _('Debug it 3'),
                'type': ARTICLE,
                'content': 'https://msrv.cf/'
            }
        }
    }
}
