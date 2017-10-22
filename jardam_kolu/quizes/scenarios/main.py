from collections import OrderedDict

from django.utils.translation import ugettext_noop as _

from ..utils import ARTICLE, QUESTION, EXTERNAL

scenario = OrderedDict({
    'start': {
        'text': _("Кто вы?"),
        'answers': [
            {
                'text': _('Жертва'),
                'type': QUESTION,
                'content': 'q-1.1'
            },
            {
                'text': _('Друг жертвы'),
                'type': QUESTION,
                'content': 'q-1.2'
            },
            {
                'text': _('Родственник жертвы'),
                'type': QUESTION,
                'content': 'q-1.3'
            }
        ]

    },
    'q-1.1': {
        'text': _("Что произошло?"),
        'answers': [

            {
                'text': _('Изнасилование'),
                'type': QUESTION,
                'content': 'q-2.1'
            },
            {
                'text': _('Избиение'),
                'type': ARTICLE,
                'content': '/articles/p/4/'
            }
        ]

    },
    'q-1.2': {
        'text': _("Что произошло?"),
        'answers': [

            {
                'text': _('Изнасилование'),
                'type': QUESTION,
                'content': 'q-2.1'
            },
            {
                'text': _('Избиение'),
                'type': ARTICLE,
                'content': 'https://zhardam.ga/articles/p/4/'
            }
        ]
    },
    'q-1.3': {
        'text': _("Что произошло?"),
        'answers': [

            {
                'text': _('Изнасилование'),
                'type': QUESTION,
                'content': 'q-2.1'
            },
            {
                'text': _('Избиение'),
                'type': ARTICLE,
                'content': '/articles/p/1/'
            }
        ]
    },
    'q-2.1': {
        'text': _('Вам нужна психологическая помощь?'),
        'answers': [

            {
                'text': _('Да'),
                'type': QUESTION,
                'content': 'q-3.1',
            },
            {
                'text': _('Нет'),
                'type': ARTICLE,
                'content': '/articles/p/4/',
            }
        ]
    },
    'q-3.1': {
        'text': _('Вы желаете бесплатную или платную психологическую помощь?'),
        'answers': [

            {
                'text': _('Бесплатную'),
                'type': ARTICLE,
                'content': '/contacts/1/',
            },
            {
                'text': _('Платную'),
                'type': ARTICLE,
                'content': '/contacts/2/',
            }
        ],
    },
    'q-2.3': {
        'text': _('Вы желаете получить юридическую помощь?'),
        'answers': [
            {
                'text': _('Да'),
                'type': QUESTION,
                'content': 'q-3.2'
            },
            {
                'text': _('Нет'),
                'type': ARTICLE,
                'content': '/articles/p/1/',
            }
        ]
    },
    'q-3.2': {
        'text': _('Вы желаете бесплатную или платную юридическую помощь?'),
        'answers': [
            {
                'text': _('Бесплатную'),
                'type': ARTICLE,
                'content': '/contacts/7/',
            },
            {
                'text': _('Платную'),
                'type': ARTICLE,
                'content': '/contacts/6/',
            }
        ],
    },
})
