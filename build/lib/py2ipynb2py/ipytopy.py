"""
Converts a python notebook to a new python script
OR
updates the corresponding python scriptj if already converted.
"""
import json
import os

def ipytopy(file_path_,file_name_):
	"""
	The driver function of this file.
	Called from the converted function in main.py.

	Parameters
	----------
	file_path_: string
	            Path of the source python script
				which has to be converted.
	file_name_: string
				Path of the corresponding converted
				python notebook.
	"""

	f=open(file_path_,"r")
	data=json.load(f)
	f.close()

	library_name='py2ipynb2py.convertor('
	l=len(library_name)

	"""fe is the file object of the file in which the program
	will write."""

	with open(file_name_,'w') as fe:
		for i in range(len(data['cells'])):
			if data['cells'][i]['cell_type']=='markdown':

				"""Special markdown syntax"""
				fe.write("'''")
				fe.write("--Markdown--")
				fe.write('\n')

				for x in data['cells'][i]['source']:
					fe.write(x)

				fe.write('\n')
				fe.write("--Markdown--")
				fe.write("'''")
				fe.write('\n')
				fe.write('\n')
			else:
				if len(data['cells'][i]['source'])==1:
					for x in data['cells'][i]['source']:
						if x[0]=='%':
							continue
						r=x.isalnum()

						if r==True:
							continue
						else:
							for y in x:
								if y.isalnum()==False and y!='_':
									if(x[:l]==library_name):
										x=x[0:-7]+'py'+x[l]+')'

									fe.write(x)
									fe.write('\n')
									fe.write('\n')
									break
				else:
					for x in data['cells'][i]['source'][:-1]:
						if x[0]=='%':
							continue

						if(x[:l]==library_name):
							x=x[0:-7]+'py'+x[l]+')'

						fe.write(x)

					x=data['cells'][i]['source'][-1]
					r=x.isalnum()

					if r==False:
						for y in x:
							if x[0]=='%':
								continue

							if y.isalnum()==False and y!='_':
								if(x[:l]==library_name):
									x=x[0:-7]+'py'+x[l]+')'
								fe.write(x)

								fe.write('\n')
								break

					fe.write('\n')
