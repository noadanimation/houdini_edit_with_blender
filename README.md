# Edit with Blender
A SOP node for Houdini users who love Blender's modeling tools.

It's a bit of a Frankenstein's monster - the seams between Houdini and Blender aren't made beautiful by this node - but it saves me a lot of time and I hope it will for you too!

Tested with Houdini 19.5 and Blender 3.5

## Installation
1) Copy the HDA to your Houdini installation's HDA folder.
2) Copy blender_importobj.py somewhere on your system - Houdini and Blender both need to see this file.

## First use
1) Place an "Edit with Blender" node.
2) Fill in the "Blender Folder" and "Blender Import Script" parameters - Blender Folder is your Blender's installation folder; Blender Import Script is where you copied "blender_importobj.py" to, including the filename
3) From the gear icon click "Save as Permanent Defaults".

## How to use
1) Link your geometry into an "Edit with Blender" node, click the "Edit in Blender" button, and Blender will open with your geometry in place ready to edit.
2) Make your edits in Blender, using all your favourite Edit or Sculpt mode tools.
3) Export your geo from Blender as an "obj" file, using the default file name and location (enable "Selected Only"), and back in Houdini click "Reload Geometry" on the Edit with Blender node.

## Tips and Gotchas
- The node will try to copy attributes and groups (other than P, N and uv) from the original geo back onto your edited/imported geo - this might not work well, especially if you add or remove points in Blender.
- If you save an empty default Blender scene (without the default cube), you can avoid having to enable "Selected Only" every time you export back to obj.
- Clicking "Edit in Blender" again will start fresh from the original geo - to continue working from your edited geo, save the Blender file and reload it later, you can export again and reload.
- The node is easiest to use if you keep the Blender filename unchanged and export an obj with that filename (the default), but you can change the node's "Input File" parameter if you want to use different file names.

Got bugs? Improvements? Ideas? Please let me know! hello@noad.co
