"""
Converts a python script to a new notebook
OR
updates the corresponding python notebook if already converted.
"""

def pytoipy(file_path_,file_name_):
	"""
	The driver function of this file.
	Called from the converted function in main.py.

	Paramters
	---------
	file_path_: string
	            Path of the source python script
				which has to be converted.
	file_name_: string
		    Path of the corresponding converted
		    python notebook.
	"""

	f=open(file_path_,"r")
	file_string=f.read()
	file_strings=file_string.split('\n')

	"""file_strings contains all the lines of the python script"""

	cell_container=[]
	"""cell_container contains the contents of the current cell being written."""
	"""id_number contains the id of the current cell being written."""
	id_number=1
	f.close()

	i=0
	r=len(file_strings)
	file_=open(file_name_,"w")
	file_.write("{")
	file_.write('"cells": [')

	while len(file_strings[-1])==0:
		file_strings=file_strings[:-1]

	file_strings.append('')
	r=len(file_strings)

	markdown_begin="'''--Markdown--"
	markdown_end="--Markdown--'''"
	"""
	The special sytax to include markdown in python scripts
	""" 

	if_markdown=False
	library_name='py2ipynb2py.convertor('
	l=len(library_name)

	for x in file_strings:
		i+=1
		x=x.replace("\t", "    ")
		
		if(x[:l]==library_name):
			x=x[:-4]+'ipynb'+x[l]+')'

		if(len(x)==15):
			if(x=="'''--Markdown--"):
				if_markdown=True
				if len(cell_container)!=0:
					build_cell(cell_container,id_number,i==r,file_,"code")
				cell_container=[]
				continue

		if(len(x)==15):
			if(x=="--Markdown--'''"):
				if_markdown=False
				id_number=build_cell(cell_container,id_number,i==r-1,file_,"markdown")
				cell_container=[]
				continue

		if(if_markdown):
			cell_container.append(x)
			continue

		if len(x)==0:
			if(len(cell_container)!=0):
				id_number=build_cell(cell_container,id_number,i==r,file_,"code")
				cell_container=[]
		else:
			cell_container.append(x)

	file_.write("],\n")
	add_metadata(file_)
	file_.close()

def build_cell(current_source,id_number,add_comma,file_,cell_type):
	"""
	Responsible for writing all of the source in a cell.

	Parameters
	----------
	current_source: list of strings 
		        which contain the source code or markdown
			of the cell to be built.
	id_number: int
	           id number of the cell being built.
	add_comma: bool
		   True if a comma has to added after writing the cell.
		   False if the current cell is the last one.
	file_: file object
	       File object in which the the program writes.
	cell_type: string
		   Specifies if the cell is markdown or code type.

	Returns
	-------
	id_number: int
		   id_number of the next cell to be built.
	"""

	current_source_parsed=""
	"""current_source_parsed is a single string which will contain
	all the string in the required format.
	"""

	for x in current_source[0:-1]:
		current_source_parsed+='"'
		r=len(x)
		pos=[]

		for i in range(r):
			if x[i]=='"':
				pos.append(i)

		if len(pos)>0:
			r=0
			for y in pos:
				current_source_parsed+=x[r:y]+'\\'
				r=y
			current_source_parsed+=x[r:]
		else:
			current_source_parsed+=x

		current_source_parsed+='\\n",'

	current_source_parsed+='"'
	x=current_source[-1]
	r=len(x)
	pos=[]

	for i in range(r):
		if x[i]=='"':
			pos.append(i)

	if len(pos)>0:
		r=0
		for y in pos:
			current_source_parsed+=x[r:y]+'\\'
			r=y
		current_source_parsed+=x[r:]
	else:
		current_source_parsed+=x
	current_source_parsed+='"'
	r=len(x)

	json_string='''
      {
		 "cell_type":"code",
		 "execution_count":null,
		 "id":"'''+str(id_number)+'",'+'''
		 "metadata": {},
		 "outputs": [],
		 "source": ['''+current_source_parsed+'''
		 ]
	  }'''

	json_string_markdown='''
      {
		 "cell_type":"markdown",
		 "id":"'''+str(id_number)+'",'+'''
		 "metadata": {},
		 "source": ['''+current_source_parsed+'''
		 ]
	  }'''

	if cell_type=="code":
		file_.write(json_string)
	else:
		file_.write(json_string_markdown)

	if not add_comma:
		file_.write(',\n')
	else:
		file_.write('\n')

	return id_number+1

def add_metadata(file_):
	"""Adds the metadata of the ipython file

	Parameters
	----------
	file_: file object
	       File object which the program writes.

	"""
		    
	json_string='''
		"metadata": {
		"kernelspec": {
		 "display_name": "Python 3 (ipykernel)",
		 "language": "python",
		 "name": "python3"
		},
		"language_info": {
		 "codemirror_mode": {
		  "name": "ipython",
		  "version": 3
		 },
		 "file_extension": ".py",
		  "mimetype": "text/x-python",
		  "name": "python",
		  "nbconvert_exporter": "python",
		  "pygments_lexer": "ipython3",
		  "version": "3.8.13"
		 }
		},
		"nbformat": 4,
		"nbformat_minor": 5
	  }'''

	file_.write(json_string)

