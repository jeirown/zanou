# zanou
Python lessons to zanou

# Lesson 1
##Setting Python Environment on Windows
1.  Download and Install [windows compiler for python packages](https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi)
2.  Download and install python package manager [pip](https://bootstrap.pypa.io/get-pip.py)  (to install just open the file)
3.  Add the environment variables to the path. 
 * Press windows button
 * Type "environment"
 * Press "Edit the system environment variables"
 * Press "Environment Variables..." button
 * Find the PATH variable under the System Variables and press "Edit ..." button
 * Add the following string to the end of the PATH variable  `;C:\Python27;C:\Python27\Scripts` and press "OK"
4.  Install python's scientific packages
 - Press windows button and type "cmd"
 - Right click command prompt and press "Run as administrator"
 - Finally install the packages with pyhon package manager(pip)
		- Type `pip install numpy` and press Enter
		- Type `pip install matplotlib` and press Enter
		- Type `pip install scipy` and press Enter
		

5. Check that everything has been done successfully
	- Open command prompt - cmd
	- Type `python` and press enter. This should invoke the python interpreter.
	- Type `import numpy` and press enter. If you din't get any errors, well done!
	- Type `import matplotlib` and press enter. If you didn't get any errors, well done!

Communicate with your teacher, [Giannis Prapas](https://www.facebook.com/giannhs.prapas), if you have any questions.
