####################################################################################################

append_to_path_if_not ${PWD}/bin
append_to_path_if_not ${PWD}/tools

append_to_ld_library_path_if_not /usr/local/stow/openjpeg2/lib/
append_to_ld_library_path_if_not /usr/local/stow/mupdf-1.3/lib/
export MUPDF_LIBRARY=/usr/local/stow/mupdf-1.3/lib/libmupdf.so

source /srv/scratch/python-virtual-env/py3-pyqt5/bin/activate
# source /srv/scratch/python-virtual-env/py3/bin/activate
append_to_path_if_not /usr/local/stow/python-3.4/bin
append_to_ld_library_path_if_not /usr/local/stow/python-3.4/lib/

append_to_python_path_if_not ${PWD}
append_to_python_path_if_not /usr/local/stow/mupdf-1.3/lib/python/

####################################################################################################
# 
# End
# 
####################################################################################################
