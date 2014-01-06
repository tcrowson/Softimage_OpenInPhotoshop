# OpenClipInImageEditor (Windows)
# 11-01-2010
# Tim Crowson

# This is a self-installing plug-in that adds a contextual menu item to open an image clip from the Clip Explorer in Photoshop.
# Install it to your user's plugins directory.
# Edit the 'PathToPhotoshop' value below to point to your executable (Photoshop or other)
# Select an image in the Clip Explorer, Right-click on it and use the "Open In Photoshop" option at the bottom.



import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
	in_reg.Author = "tcrowson"
	in_reg.Name = "OpenClipInPSPlugin"
	in_reg.Major = 1
	in_reg.Minor = 0

	in_reg.RegisterCommand("OpenClipInPS","OpenClipInPS")
	in_reg.RegisterMenu(constants.siMenuSEGeneralContextID,"OpenClipInPS_Menu",false,false)
	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

def OpenClipInPS_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = ""
	oCmd.ReturnValue = true

	return true

def OpenClipInPS_Execute(  ):

	Application.LogMessage("OpenClipInPS_Execute called",constants.siVerbose)
	# 
	import os
	from subprocess import Popen

	if not "Open clip in PS" in (str(x.Name) for x in Application.Preferences.Categories):
		Application.PathPrefSetup()
		XSIUIToolkit.MsgBox("Before you can use this plug-in, you'll need to set the path\rto your image editor in the preferences.\r\rPreferences > Custom > Open clip in PS",64,"Open Clip in PS - Setup")
		Application.InspectPreferences("Open Clip in PS")
	elif "Open clip in PS" in (str(x.Name) for x in Application.Preferences.Categories):

		PathToPhotoshop = Application.GetValue("preferences.Open clip in PS.Path")
		if PathToPhotoshop == "":
			XSIUIToolkit.MsgBox("Please set the path to the image editor in the preferences\r\rPreferences > Custom > Open clip in PS",64,"Open Clip in PS")
			Application.InspectPreferences("Open Clip in PS")
		else:
			sel = Application.Selection(0)
			rawPath = chr(34) + sel.Source.Parameters("Path").Value + chr(34)
			exe = chr(34) + PathToPhotoshop + chr(34) + " "
			Application.LogMessage("OpenClipInPS:   opening clip '%s' in image editor"%(sel.Name))
			Popen(exe + rawPath)
	# 
	return true

def OpenClipInPS_Menu_Init( in_ctxt ):
	oMenu = in_ctxt.Source
	oMenu.Filter = "clip"
	oMenu.AddCommandItem("Open Clip in Photoshop","OpenClipInPS")
	return true

