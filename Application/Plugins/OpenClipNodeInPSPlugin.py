# OpenClipNodeInImageEditor (Windows)
# 11-01-2010
# Tim Crowson

# This is a self-installing plug-in that adds a contextual menu item to open an image clip from the Render Tree in Photoshop.
# Install it to your user's plugins directory.
# Edit the 'PathToPhotoshop' value below to point to your executable (Photoshop or other)
# Right-click on an image clip in the Render Tree and use the "Open In Photoshop" option at the bottom.



import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
	in_reg.Author = "tcrowson"
	in_reg.Name = "OpenClipNodeInPSPlugin"
	in_reg.Major = 1
	in_reg.Minor = 0

	in_reg.RegisterCommand("OpenClipNodeInPS","OpenClipNodeInPS")
	in_reg.RegisterMenu(constants.siMenuRTNodeContextID,"OpenClipNodeInPS_Menu",False,True)
	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

def OpenClipNodeInPS_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = ""
	oCmd.ReturnValue = true
	return true
	
def OpenClipNodeInPS_Execute(  ):

	Application.LogMessage("OpenClipNodeInPS_Execute called",constants.siVerbose)
	# 
	import os
	from subprocess import Popen

	if not "Open clip in PS" in (str(x.Name) for x in Application.Preferences.Categories):
		Application.PathPrefSetup()
		XSIUIToolkit.MsgBox("Before you can use this plug-in, you'll need to set the path\rto your image editor in the preferences.\r\rPreferences > Custom > Open clip in PS",64,"Open Clip in PS - Setup")
		Application.InspectPreferences("Open Clip in PS")
	elif "Open clip in PS" in (str(x.Name) for x in Application.Preferences.Categories):
		PathToPhotoshop = Application.GetValue("preferences.Open clip in PS.Path")

		app = Application
		oRoot = app.ActiveSceneRoot

		oLayout = app.Desktop.ActiveLayout
		oViewColl = oLayout.Views

		oVM = Application.Desktop.ActiveLayout.Views( "vm" )
		curView = oVM.GetAttributeValue ("viewportundermouse")
		curViewType = oVM.GetAttributeValue("viewport:%s"%(curView))

		selected = []

	
		for x in oViewColl:
			if x.Type == 'Render Tree':
				selected.append(x.GetAttributeValue('selection'))
			elif curViewType == 'Render Tree':
				selected.append(x.GetAttributeValue('selection'))
		for y in selected:
			app.SelectObj(y, "", "")
			sel = app.Selection(0)
			if sel.Type == "ImageClip":
				rawPath = chr(34) + sel.Source.Parameters("Path").Value + chr(34)
				exe = chr(34) + PathToPhotoshop + chr(34) + " "
				Popen(exe + rawPath)
	# 
	return true


def OpenClipNodeInPS_Menu_Init( in_ctxt ):
	oMenu = in_ctxt.Source
	node = in_ctxt.GetAttribute("Target")(0)
	if node.Type == "ImageClip":
		oMenu.AddCommandItem("Open In Photoshop","OpenClipNodeInPS")
	return true

