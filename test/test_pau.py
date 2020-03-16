from django.test.testcases import TestCase

from tuitse import THAU_JI, LIAN_JI, pau


class TshiGiam(TestCase):

    def tearDown(self):
        kiatko = pau(self.guan)
        self.assertEqual(kiatko, self.bang)

    def test_kantan(self):
        self.guan = [
            ('我', 'guá', THAU_JI, True),
        ]
        self.bang = [
            [
                {
                    'hanji': '我',
                    'lomaji': 'guá',
                    'si_tioh': True
                }
            ]
        ]

    def test_lakli(self):
        self.guan = [
            ('豬', '', THAU_JI, False),
            ('仔', 'á', THAU_JI, True),
            ('', 'ti', LIAN_JI, False),
        ]
        self.bang = [
            [
                {
                    'hanji': '豬',
                    'lomaji': '\u00A0',
                    'si_tioh': False
                }
            ], [
                {
                    'hanji': '仔',
                    'lomaji': 'á',
                    'si_tioh': True
                }, {
                    'hanji': '\u00A0',
                    'lomaji': '-',
                    'si_tioh': True
                }, {
                    'hanji': '\u00A0',
                    'lomaji': 'ti',
                    'si_tioh': False
                }
            ]
        ]

    def test_soojitiau_lianjihu(self):
        self.guan = [
            ('會', 'e7', 1, True), ('當', 'tang3', 2, True),
        ]
        self.bang = [
            [
                {
                    'hanji': '會',
                    'lomaji': 'e7',
                    'si_tioh': True
                }, {
                    'hanji': '\u00A0',
                    'lomaji': '-',
                    'si_tioh': True
                }, {
                    'hanji': '當',
                    'lomaji': 'tang3',
                    'si_tioh': True
                }
            ]
        ]

    def test_lianjihu(self):
        self.guan = [
            ('會', 'ē', 1, True), ('當', 'tàng', 2, True),
        ]
        self.bang = [
            [
                {
                    'hanji': '會',
                    'lomaji': 'ē',
                    'si_tioh': True
                }, {
                    'hanji': '\u00A0',
                    'lomaji': '-',
                    'si_tioh': True
                }, {
                    'hanji': '當',
                    'lomaji': 'tàng',
                    'si_tioh': True
                }
            ]
        ]
