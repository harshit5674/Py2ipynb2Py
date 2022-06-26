# Py2ipynb2Py

__py2ipynb2py__ is a python module which aims to bridge the gap between Python scripts and Python notebooks by letting the user convert .py to .ipynb and vice versa and lets the user keep both the files in sync.

# Why use it

Python notebooks and scripts serve almost the same function that is running python code, yet they appear to be such different entities with different pros and cons.

## Jupyter notebooks disadvantages
*__Dependencies__.In some cases, the notebook imports libraries that are only installed on the computer of a data analyst (locally). The issue with such a scenario is that a programmer using a different version of the same library, such as NumPy, may experience the setback of the actual 
production calculations not agreeing with those in the research.
*__Object Oriented Paradigm__.Difficult to follow using notebooks
*Not possible to reproduce the outcomes from Jupyter Notebook received from a local execution.
*Cannot give a definite structure we can give by maintaining scripts
*Notebook results performed by one machine might differ when running on another computer in the same group bearing in mind that the machines might have some caching differences.

## Jupyter notebook Advantages
*You can execute the code and see the magic instantly.
*You can run cells independently and see several outputs without running all of the program.
*Easy and coonvinient to use.

With py2ipynb2py you can easily convert .py to .ipynb and vice versa, it also then keeps both the files in sync. Markdows are preserved, i.e. even if your jupyter notebook has images these are conserved when you convert it to .py and that .py file is compilable even while maintaining all the markdowns. You can even add markdows in python files using py2ipynb2py's special syntax.

While the famouse nbconvert library lets you convert .ipynb to .py, it does not let you convert .py to .ipynb and there is no feature to keep both the file in sync and maintainble.

#Installation


