
# This file has been generated at Mon Nov 14 05:45:36 2016

from openalea.core import *


__name__ = '__my package__'

__editable__ = True
__description__ = ''
__license__ = ''
__url__ = ''
__alias__ = []
__version__ = ''
__authors__ = ''
__institutes__ = ''
__icon__ = ''


__all__ = ['_140445423187152', 'my_model_my_model']



_140445423187152 = CompositeNodeFactory(name='pygmalion_interface',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[  {  'desc': '', 'interface': IStr, 'name': 'parameter_file', 'value': './p.txt'},
   {  'desc': '', 'interface': IStr, 'name': 'output_file', 'value': './y.txt'}],
                             outputs=[],
                             elt_factory={  2: ('openalea.pandas.io', 'read_csv'),
   3: ('openalea.pandas.io', 'to_csv'),
   4: ('openalea.flow control', 'annotation'),
   5: ('openalea.flow control', 'annotation'),
   6: ('__my package__', 'my_model')},
                             elt_connections={  11051432: (6, 0, 3, 0),
   11051456: ('__in__', 1, 3, 1),
   11051480: (2, 0, 6, 0),
   11051504: ('__in__', 0, 2, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'read_csv',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -78.09077876008774,
         'posy': 4.685446725605264,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'to_csv',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 12.572040268985262,
         'posy': 201.5029647704703,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'id': 4,
         'posx': -85.11894884849565,
         'posy': -116.35526035253078,
         'txt': u'Program Parameters'},
   5: {  'id': 5,
         'posx': -215.53054937784225,
         'posy': -31.236311504035104,
         'txt': u'Reading Parameters'},
   6: {  'block': False,
         'caption': 'my_model',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -82.68008088324697,
         'posy': 90.60830781725693,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': -10.489049203228081,
                'posy': -127.6525943352895,
                'priority': 0,
                'use_user_color': False,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (1, "','"),
         (2, '0'),
         (3, 'None'),
         (4, 'None'),
         (5, 'None'),
         (6, 'None'),
         (7, 'False'),
         (8, 'None'),
         (9, 'None'),
         (10, 'False'),
         (11, 'None'),
         (12, '0'),
         (13, 'None'),
         (14, 'False'),
         (15, 'None'),
         (16, 'None')],
   3: [  (2, "','"),
         (3, "''"),
         (4, 'None'),
         (5, 'True'),
         (6, 'True'),
         (7, 'None'),
         (8, "'w'"),
         (9, 'None'),
         (10, 'None')],
   4: [],
   5: [],
   6: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'useUserColor': False, 'position': [-78.09077876008774, 4.685446725605264], 'userColor': None},
   3: {'useUserColor': False, 'position': [12.572040268985262, 201.5029647704703], 'userColor': None},
   4: {'visualStyle': 1, 'position': [-85.11894884849565, -116.35526035253078], 'color': None, 'text': u'Program Parameters', 'textColor': None, 'rectP2': (-1, -1)},
   5: {'visualStyle': 1, 'position': [-215.53054937784225, -31.236311504035104], 'color': None, 'text': u'Reading Parameters', 'textColor': None, 'rectP2': (-1, -1)},
   6: {'position': [-82.68008088324697, 90.60830781725693], 'userColor': None, 'useUserColor': False},
   '__in__': {'useUserColor': False, 'position': [-10.489049203228081, -127.6525943352895], 'userColor': None},
   '__out__': {'useUserColor': True, 'position': [0, 0], 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




my_model_my_model = Factory(name='my_model',
                authors=' (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='my_model',
                nodeclass='my_model',
                inputs=[{'interface': IInterface, 'name': 'p', 'value': None, 'desc': ''}],
                outputs=[{'interface': IInterface, 'name': 'system_observation', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




