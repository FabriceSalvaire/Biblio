####################################################################################################
#
# This file is Autogenerated by make-ConfigInstall
#
####################################################################################################

####################################################################################################

from pathlib import Path

import Babel.backend.Tools.Path as PathTools # due to Path class

####################################################################################################

_this_file = Path(__file__).resolve()

class Path:

    babel_module_directory = _this_file.parents[1]
    config_directory = _this_file.parent

    # Fixme
    share_directory = babel_module_directory.parent.joinpath('share')
    qml_path = share_directory.joinpath('qml')

    ##############################################

    @classmethod
    def join_share_directory(cls, *args):
        return cls.share_directory.joinpath(*args)

    ##############################################

    @classmethod
    def join_qml_path(cls, *args):
        return cls.qml_path.joinpath(*args)

####################################################################################################

class Logging:

    default_config_file = 'logging.yml'
    directories = (Path.config_directory,)

    ##############################################

    @classmethod
    def find(cls, config_file):

        return PathTools.find(config_file, cls.directories)

####################################################################################################

class Icon:

    icon_directory = Path.join_share_directory('icons')

    ##############################################

    @classmethod
    def find(cls, file_name, size):

        icon_directory = cls.icon_directory.joinpath('{0}x{0}'.format(size))
        return PathTools.find(file_name, (icon_directory,))

####################################################################################################

class Corpus:

    # Language ID are defined in Corpus.LanguageID
    languages = ('en', 'fr')
    sqlite_path = Path.join_share_directory('data', 'corpus', 'corpus.sqlite')
