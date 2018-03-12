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

####################################################################################################

from .BritishNationalCorpus import Tags as en_tags
from .FrenchCorpus import Tags as fr_tags

from .Tags import TagRegistry
# from .CorpusRegistry import CorpusRegistry

####################################################################################################

tag_registry = TagRegistry()
# corpus_registry = CorpusRegistry() # lazy