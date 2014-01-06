Softimage_OpenInPhotoshop
=========================

This addon registers new context-menu commands for clips in the Clip Explorer and the Shader Tree, allowing you to open the target clip in the image editor of your choosing (using Photoshop here), or explore the image's location on disk. The first time one of the commands is run, a preference is added to contain the path to the image editing application.

There is a limitation in Softimage that prevents this plugin from working correctly in Shader Trees that are not floating. So if one of your main viewports is set to be a Shader Tree, the command will fail.
