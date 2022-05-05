from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

import sys

#Uncomment the below and in 'Executable' to NOT include a console when the application launches and runs.
#base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(
    	'myapplication.py', 
    	#base=base, 
    	target_name = 'PyQt_Example_App',
    	icon="unicorn.ico",
    )
]

includeFiles = [
	'applicationinterface.ui',										#QtDesigner UI file
	'unicorn.ico', 								#Application Icon file
	#'ClientCertificates/', 									#Folder containing all of the auth certificates
	'py_SAPHANA_GetIntervalData5minMapMethod.py', 			#Python file with interval data and RRP function in it.
	#'mkl_intel_thread.1.dll',								#App would brick without it, added from Anaconda3 folder.
    #Include this Anaconda3 folder to avoid "This application filed to start because it could not load Qt Platform plugin "windows"
	'C:/Users/a139540/Anaconda3/Library/plugins/platforms/'	#Including after encountered strange error that needed it
]

#Create the options object for the build exe command
build_exe_options = {
	'packages': [], 
	'excludes': [],
	'include_files': includeFiles
}

# Create data specific to the msi file
msi_data = {
	"Shortcut": [
	    (
	        "DesktopShortcut",        							# Shortcut
	        "DesktopFolder",          							# Directory_
	        "PyQt_Example_App",        		        # Name
	        "TARGETDIR",              							# Component_
	        "[TARGETDIR]PyQt_Example_App.exe",      # Target
	         None,                     							# Arguments
	         None,                     							# Description
	         None,                    							# Hotkey
	         None,                 								# Icon  "telstraAGLlogosmall.ico"
	         None,                     							# IconIndex
	         None,                     							# ShowCmd
	        'TARGETDIR'               							# WkDir
	    )
	],
	"Icon": [
		(
			"IconId",
			"unicorn.ico"
		)
	]
}
#Create the options object for the msi build command
bdist_msi_options = {
    'data': msi_data,
    'add_to_path': False,
    'initial_target_dir': r'[DesktopFolder]\%s' % ("PyQt_Example_App"),
    "upgrade_code": "{96a85bac-52af-4019-9e94-3afcc9e1ad0e}",
}

setup(
	name='PyQt_Example_App',
    description = 'https://github.com/rphelanagl/PyQt_Example_App',
    options = {'build_exe': build_exe_options, "bdist_msi" : bdist_msi_options},
    executables = executables
)