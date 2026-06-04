# NeMO Fiji Plugin

**Neuro Mask Organizer (NeMO)** is a Fiji plug-in for anatomical mask segmentation. **Fiji** is a widely used open-source image-processing platform in the biological sciences. NeMO enables users to manually annotate anatomical masks, compare them with registered or predicted masks, and correct overlaps between masks. The software also supports hybrid workflows that combine manual annotation with automated segmentation. It currently provides two automated approaches:.   
1. **Morphological contour interpolation**, which propagates annotations between labeled slices.
2. **Deep-learning–based segmentation**, which predicts masks from image data using trained models.

In this tutorial, we provide detailed installation instructions and a step-by-step example using a test project.

---

**System requirements**

The minimal requirements for running NeMO are:
1. Memory: 16-32 GB
2. Operating system: Windows 10+11, Linux, MacOS
3. Processor: 32-64 bit
4. Latest version of Fiji

---

**Installation instructions**

Download the “NeMO.jar” from the github repository and copy it to the Fiji “plugins” directory (encircled red in the images below).
<img src="images/NeMO1.png"/>
<img src="images/NeMO2.png"/>
---

**Project structure**

Download the demo project("medakasegmentation.zip") and unzip it. If you want to annotate your custom data, please download "regionssegmentation.zip" and unzip it. The project structure is shown in the image below.

<img src="images/NeMO_PROJECT.png"/>


The data folder contains several subfolders, each serving a specific purpose. Most of these folders are automatically managed by NeMO and are used to organize annotation data, intermediate results, model predictions, and backups.

1. **history** – Stores historical versions of the masks.
2. **interslicetiff** – Contains TIFF files generated through morphological contour interpolation.
3. **models** – Stores regions predicted by the segmentation models.
4. **regions_backup** – Contains automatically generated backups of expert-annotated regions.
5. **regions** – Stores expert-annotated regions in a compressed format.
6. **slices** – Contains the reference image stack used for annotation.
7. **tiff** – Stores the regions annotated by experts in TIFF format.


Open the project JSON file (e.g., **medakasegmentation.json**). If you would like to annotate your own dataset, first copy the reference TIFF stack into the slices folder. Then, update the **referenceFile** field in the JSON file so that it points to your reference stack, as highlighted by the red circle in the images below.

After saving the changes, the project will load your custom reference data for annotation.   

<img src="images/NeMO_PROJECTFILE.png"/>

One can also find a list of environments in the project JSON file. NeMO relies on Python scripts and these Conda environments to perform image registration and segmentation tasks.

To use the **Morphological Contour Interpolation** feature, users must first create the required Conda environment and install the necessary packages using the commands provided below.

1. conda create --name interslice
2. conda install pip
3. pip install itkwasm-morphological-contour-interpolation

Please also update the path of **pythonfile** related to Morphological Contour Interpolation in the project JSON file.

Instructions for setting up and using the **image registration** and **deep-learning–based segmentation** modules will be provided in their respective tutorials.

---
Open the Fiji platform and the NeMO plugin will be enlisted in the Fiji “plugins” tab (encircled red in the image below). 

<img src="images/NeMO3.png"/>

---

Click the “NeMO” button and select the project JSON file (e.g., **medakasegmentation.json**) (shown in the image below). 
<img src="images/NeMO_SELECTJSON.png"/>

The project will be loaded and the NeMO window will appear on the screen as shown below.

<img src="images/NeMO4.png"/>

If you would like to add a new region, click the Add button (highlighted by the red rectangle in the image above). The following window will then appear on the screen.
Enter the name of the region, including the .zip extension (e.g., forebrain.zip), and click Open to create the new region.

<img src="images/NeMO_ADDREGION.png"/>

---

To annotate a region, first select the Polygon ROI tool from the Fiji toolbar. Draw the ROI on the current slice and click the **add roi** to save the annotation for that slice.
Begin by annotating the first and last slices of the region. Then, annotate every 5–8 slices in between, depending on the complexity and variability of the structure.

These annotations can later be used for interpolation or as training data for automated segmentation methods. 

Finally, click "ISI Selected Region" in the Others panel. This will start the Morphological Contour Interpolation process for the currently selected region in a separate thread.

The interpolation will run in the background, allowing you to continue working within Fiji. Once the process is complete, a confirmation message will be displayed in the Fiji Log window. 

You can then review the generated interpolated tiff in the **interslicetiff** folder and corresponding compressed rois in the **models** folder.