# Image Labeling Tool

This project provides a Tkinter-based GUI application for labeling and preprocessing images. The tool allows users to load images from a specified directory, apply various preprocessing techniques like contour detection and color masking, and save the results to an output directory. Additionally, it includes interactive controls for fine-tuning the preprocessing parameters through OpenCV trackbars, making it easy to customize the output for each image.

[![Preview](https://github.com/user-attachments/assets/80427b32-99e9-477c-b765-ceaa52ae55c5)](https://github.com/user-attachments/assets/80427b32-99e9-477c-b765-ceaa52ae55c5)




## Features

The application begins by loading images from the specified directory (`main_path`) and displays them in a Tkinter GUI. Users can navigate through the images using Next and Previous buttons, and each image's preprocessing results are updated in real-time based on the trackbar settings. The preprocessing workflow involves several steps:

1. **Contour Detection**: The tool detects the contours in the image by converting it to grayscale, applying a binary threshold, and drawing the contours on a blank image.
2. **Color Masking**: Users can specify upper and lower HSV bounds for masking specific regions in the image. The selected mask is then converted to an RGB format.
3. **Combined Results**: The tool overlays the contour and mask results onto the original image, generating a final visualization for each image.

The preprocessing parameters, including HSV bounds and threshold value, can be adjusted dynamically using trackbars displayed in an OpenCV window named "Settings."

The tool also provides an option to save the processed images. When saved, the contour and masked images are stored in separate directories under the specified `output_path`. If the output directory does not exist, it is automatically created.

## How to Use

1. **Run the Script**: Execute the Python script to launch the Tkinter GUI.
2. **Navigate Images**: Use the Next and Previous buttons to cycle through the images in the directory.
3. **Adjust Parameters**: Modify the high and low HSV values or the threshold value using the trackbars to customize the preprocessing results.
4. **Save Results**: Click the Save button to store the contour and mask results for the current image. The saved files will be organized into separate directories under the specified output path.

## Code Overview

- **Image Preprocessing**: The script uses OpenCV functions for contour detection (`cv.findContours`) and color masking (`cv.inRange`) to preprocess each image.
- **Interactive GUI**: The GUI is built with Tkinter and allows users to visualize and interact with the preprocessing results in real-time.
- **Trackbars**: OpenCV trackbars provide an intuitive way to adjust preprocessing parameters dynamically.
- **File Management**: The script ensures that output directories are created if they do not already exist, organizing the saved results into separate folders.

## Customization

The script is easily customizable. Users can modify the following:

- `main_path`: Path to the directory containing input images.
- `output_path`: Directory where the processed images will be saved.
- `image_shape`: Desired dimensions for resizing the input images.
- Initial HSV and threshold values: These can be adjusted in the script or through the GUI.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- Tkinter (comes pre-installed with Python)
- PIL (Python Imaging Library, install using `pip install pillow`)

## Installation

1. Clone or download the repository.
2. Install the required dependencies using pip:
   ```bash
   pip install opencv-python pillow
   ```
3. Update the paths for `main_path` and `output_path` in the script as needed.

## Conclusion

This Image Labeling Tool is designed to simplify the process of preprocessing and labeling images for machine learning or other analytical tasks. The interactive interface and adjustable parameters make it a versatile and user-friendly tool for handling image datasets.

