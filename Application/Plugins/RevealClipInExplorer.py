# Reveal Clip in Explorer (Windows)
# 11-01-2010
# Tim Crowson

# Adds option to show the selected clip in Explorer.


import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
	in_reg.Author = "tcrowson"
	in_reg.Name = "RevealClipInExplorerPlugin"
	in_reg.Major = 1
	in_reg.Minor = 0

	in_reg.RegisterCommand("RevealClipInExplorer","RevealClipInExplorer")
	in_reg.RegisterMenu(constants.siMenuRTNodeContextID,"RevealClipInExplorer_Menu",False,True)
	in_reg.RegisterMenu(constants.siMenuSEGeneralContextID,"RevealClipInExplorer_Menu",False,True)

	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

def RevealClipInExplorer_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = ""
	oCmd.ReturnValue = true
	return true
	
def RevealClipInExplorer_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = ""
	oCmd.ReturnValue = true
	return true

def RevealClipInExplorer_Execute(  ):

	Application.LogMessage("RevealClipInExplorer_Execute called",constants.siVerbose)
	# 
	import os
	app = Application
	oRoot = app.ActiveSceneRoot
	oLayout = app.Desktop.ActiveLayout
	oViewColl = oLayout.Views
	oVM = Application.Desktop.ActiveLayout.Views( "vm" )
	curView = oVM.GetAttributeValue ("viewportundermouse")
	curViewType = oVM.GetAttributeValue("viewport:%s"%(curView))
	selected = []
	sel = app.Selection
	
	for each in sel:
		if each.Type == "ImageClip":
			rawPath = each.Source.Parameters("Path").Value
			oFolder = rawPath[:rawPath.rfind('\\')+1]
			os.startfile(oFolder)
	for x in oViewColl:
		if x.Type == 'Render Tree':
			selected.append(x.GetAttributeValue('selection'))
		elif curViewType == 'Render Tree':
			selected.append(x.GetAttributeValue('selection'))
	for y in selected:
		app.SelectObj(y, "", "")
		sel = app.Selection(0)
		if sel.Type == "ImageClip":
			rawPath = sel.Source.Parameters("Path").Value
			oFolder = rawPath[:rawPath.rfind('\\')+1]
			os.startfile(oFolder)
			
	# 
	return true


def RevealClipInExplorer_Menu_Init( in_ctxt ):
	oMenu = in_ctxt.Source
	node = in_ctxt.GetAttribute("Target")(0)
	if node.Type == "ImageClip":
		oMenu.AddCommandItem("Show in Explorer","RevealClipInExplorer")
	return true

