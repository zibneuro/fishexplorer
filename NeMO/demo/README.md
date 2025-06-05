# NeMO Demo
The NeMO consists of several sub-panels; The “Selection panel” shows the currently selected region for modification 
and the currently selected roi (region of interest); The “Regions panel” (highlighted  by red arrow in the image below) 
shows the list of the regions to be modified; The “Color channel panel” (highlighted  by yellow arrow in the image below) 
allows users to load the masks in different colours. The “Others panel ” consist of several utility buttons: (1) “add region” allow users to add a new region, (2) “remove region” allow users to delete the current selected region, (3) “masks to tiff” convert all the masks to the tiff stacks, (4) “change stack” allows to change the reference image stack, (5) “open overlap panel”, and (6) “open DL panel”.

The central window of the NeMO consists of the reference image stack. All the selected masks and color masks are overlaid on 
top of the reference stack. The roi function panel (highlighted by green arrow in the image below) consists of several functions 
(1) “and” , (2) “or”, (3) “xor”, (4) “not”, (5) “add roi” allows to add currently drawn region of interest to the region, 
The name will be automatically assigned to the roi  (6) “update roi” allows to save the currently selected roi, 
(7) “remove roi” will delete the currently selected roi, (8) “clear rois” delete all the rois in the current slice, 
(9) “mirror left” copy the selected roi to the left hemisphere, (10) “mirror right” copy the selected roi to the right hemisphere, 
(11) “copy prev. Slice” copy the selected roi to the previous slice and (12) “copy next slice” copy the selected roi to the next slice of the image. 
The “model rois” panel shows a list of roi’s labeled or generated using the specific deep learning/registration model. 
The “updated rois panel” (highlighted by blue arrow in the image below) shows a list of roi’s labeled for the current slice,
user can select the roi by clicking on the roi name, which will then be displayed in yellow in the central window.


**Basic procedure of drawing masks**

To begin with, load an imaging stack using the “Change stack button” that you will make masks based on. Move to the slice where you want to draw a mask. Choose the region name that you want to make masks in the “Regions panel” (red arrowhead).
Draw a region of interest and you’ll see a yellow mask overlapping on the stack. Push the “Add roi” button then the mask is stored. 
When a user wants to fix the mask partially by adding or removing a small area, first select the mask in the “updated rois panel” (blue arrowhead) that user wants to fix. Then draw a region of interest and then push either “and” for adding it to the existing one or “not” for removing the part.
If the region mask also exists in the other hemisphere and the regions are symmetric, then push either “mirror right” or “mirror left” then a horizontally-mirrored mask gets added .
If the user wants to erase the roi, select the mask and then push “remove roi”.
If the user wants to copy the mask to the next or previous slice, select the mask and push “copy prev. slice” or “copy next slice”. 
Once a user finishes with fixing the masks, you can push “update roi” to finalize an update

