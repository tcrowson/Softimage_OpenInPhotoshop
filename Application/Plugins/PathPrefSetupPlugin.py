# PathPrefSetupPlugin (Windows)
# 11-01-30
# Tim Crowson

# This adds a custom preference to house the path to image editor used by the "OpenInPS" scripts.



import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
	in_reg.Author = "tcrowson"
	in_reg.Name = "PathPrefSetup"
	in_reg.Major = 1
	in_reg.Minor = 0

	in_reg.RegisterCommand("PathPrefSetup","PathPrefSetup")
	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

def PathPrefSetup_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Adds a custom preference for housing the path to the image editor"
	oCmd.ReturnValue = true

	return true

def PathPrefSetup_Execute(  ):

	Application.LogMessage("PathPrefSetup_Execute called",constants.siVerbose)
	# 
	from win32com.client import constants as c
	custPref = Application.SIAddCustomParameter("Scene_Root", "Path", c.siString, 0, 0, 1, "", 4, 0, 1, "", "")
	Application.InstallCustomPreferences("CustomPSet", "Open clip in PS")

	# 
	return true

