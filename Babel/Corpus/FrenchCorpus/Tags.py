####################################################################################################
#
# Babel - A Bibliography Manager
# Copyright (C) 2018 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

from ..Tags import TagsAbc

####################################################################################################

class Tags(TagsAbc):

    __language__ = 'fr'

    __tags__ = {
        'ADJ': 'Adjectif',
        'ADJ:dem': 'Adjectif démonstratif',
        'ADJ:int': 'Adjectif interrogatif',
        'ADJ:ind': 'Adjectif indéfini',
        'ADJ:num': 'Adjectif numérique',
        'ADJ:pos': 'Adjectif possessif',
        'ADV': 'Adverbe',
        'ART:def': 'Article défini',
        'ART:ind': 'Article indéfini',
        'AUX': 'Auxiliaire',
        'CON': 'Conjonction',
        'LIA': "Liaison euphonique (l')",
        'NOM': 'Nom commun',
        'ONO': 'Onomatopée',
        'PRE': 'Préposition',
        'PRO:dem': 'Pronom démonstratif',
        'PRO:ind': 'Pronom indéfini',
        'PRO:int': 'Pronom interrogatif',
        'PRO:per': 'Pronom personnel',
        'PRO:pos': 'Pronom possessif',
        'PRO:rel': 'Pronom relatif',
        'VER': 'Verbe',
    }

    __noun_tags__ = ('NOM')
