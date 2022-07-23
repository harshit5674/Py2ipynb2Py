from .ipytopy import ipytopy
from .pytoipy import pytoipy
import os.path

def convertor(file_path_):
	"""Main function which is called from the source.
	   This function checks the file extension to call pytoipy or ipytopy.
	   This function creates a corresponding converted file if it doesnt exits.
	
	Parameters
	----------
	file_path_: string
				Path of the source file from where the function
				has been called.
	
	"""
	if(file_path_[-2:]=='nb'):
		"""This suggests that the file is a python notebook."""

		new_file_path_=file_path_[:-5]+'py'

		"""new_file_path_ denotes the path of the converted python script."""

		if os.path.isfile(new_file_path_):
			ipytopy(file_path_,new_file_path_)
		else:
			open(new_file_path_,'w').close()
			ipytopy(file_path_,new_file_path_)
	else:
		"""This suggests that the file is a python script."""

		new_file_path_=file_path_[:-2]+'ipynb'

		"""new_file_path_ denotes the path of the converted python notebook."""

		if os.path.isfile(new_file_path_):
			pytoipy(file_path_,new_file_path_)
		else:
			open(new_file_path_,'w').close()
			pytoipy(file_path_,new_file_path_)

