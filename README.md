# Aerial Pool Detection Tool

This repository contains my submission for the Sanadtech PFE technical test. The project is a Command Line (CL) tool designed to detect swimming pools in aerial imagery using computer vision. It supports various pool shapes (rectangular, oval, and irregular) and handles complex environments like resorts or residential areas.

## Project Deliverables
- **CLI Script**: A Python script to process images.
- **coordinates.txt**: A structured text file containing the boundary points of detected pools.
- **output_image.jpg**: The result image with red outlines and labels.

## Technical Approach

Instead of a deep learning model which requires large datasets and high computational power, I implemented a robust image processing pipeline using **OpenCV**. This approach is highly efficient for real-time processing and easy to integrate.

### Logic Pipeline:
1. **Color Space Transformation**: The image is converted to **HSV** (Hue, Saturation, Value). This allows for better isolation of "Pool Blue" wavelengths regardless of lighting brightness.
2. **Spectral Filtering**: I applied specific saturation and value thresholds to distinguish vibrant pool water from neutral-colored objects like gray roofs, asphalt, or light green tiles.
3. **Morphological Refinement**: Using elliptical kernels, the script performs "Closing" and "Opening" operations to bridge gaps (like tree branches over a pool) and remove small noise (like umbrellas or chairs).
4. **Geometric Validation**: To ensure accuracy, shapes are filtered by **Solidity**. This ensures that only solid water bodies are detected, ignoring scattered shadows or blue artifacts.
5. **Contour Approximation**: The script uses a very low epsilon value in the approximation phase to ensure the red outline follows the organic curves of irregular pools perfectly.

## Setup Instructions

### 1. Requirements
- Python 3.8 or higher
- OpenCV (`opencv-python`)
- NumPy

### 2. Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/sanadtech-pool-detection.git
cd sanadtech-pool-detection
pip install -r requirements.txt
```
## Usage

Run the detection script from the project root:

    python src/pool_detector.py path/to/your/image.jpg

The script generates two output files in the project root:

- output_image.jpg  
  The image with detected pools outlined and labeled

- coordinates.txt  
  A detailed list of the points forming the shape of each detected pool

## Sample Results

The following examples demonstrate the script's ability to handle different environments, from residential backyards to complex resort layouts.

### Detection Output

Input Image  
![Input Image](samples/input_sample.jpg)

Detection Result  
![Detection Result](output_image.jpg)

Note: The script successfully filters out shadows and nearby gray structures while maintaining the curved boundaries of the water body.

## Coordinate Format

The coordinates.txt file provides high-density points for each pool, sorted by area:

    --- Pool 1 ANALYSIS ---
    Precision Points: 112 | Area: 15420 px
    pt1: 412,105
    pt2: 415,108
    ...

## Repository Structure

    sanadtech-pool-detection/
    ├── src/
    │   └── pool_detector.py    # Main CLI detection logic
    ├── samples/                # Sample input images for testing
    ├── requirements.txt        # Required Python libraries
    ├── coordinates.txt         # Generated coordinates (last run)
    ├── output_image.jpg        # Annotated result (last run)
    └── README.md               # Project documentation
