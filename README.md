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
![Detection Result](h.jpg)


## Coordinate Format

The coordinates.txt file provides high-density points for each pool, sorted by area:

   --- POOL 1 ANALYSIS ---
Precision Points: 77 | Area: 884 px
Point 001: [188, 62]
Point 002: [187, 63]
Point 003: [186, 63]
Point 004: [185, 64]
Point 005: [184, 64]
Point 006: [181, 67]
Point 007: [180, 67]
Point 008: [178, 69]
Point 009: [177, 69]
Point 010: [175, 71]
Point 011: [175, 78]
Point 012: [176, 78]
Point 013: [177, 79]
Point 014: [178, 79]
Point 015: [179, 80]
Point 016: [179, 84]
Point 017: [180, 84]
Point 018: [181, 85]
Point 019: [182, 85]
Point 020: [183, 86]
Point 021: [184, 86]
Point 022: [185, 87]
Point 023: [185, 88]
Point 024: [186, 89]
Point 025: [186, 94]
Point 026: [187, 94]
Point 027: [188, 95]
Point 028: [189, 95]
Point 029: [190, 96]
Point 030: [191, 96]
Point 031: [192, 97]
Point 032: [192, 99]
Point 033: [193, 100]
Point 034: [193, 101]
Point 035: [194, 101]
Point 036: [196, 103]
Point 037: [196, 104]
Point 038: [197, 104]
Point 039: [198, 105]
Point 040: [199, 104]
Point 041: [200, 104]
Point 042: [201, 103]
Point 043: [202, 103]
Point 044: [205, 100]
Point 045: [206, 100]
Point 046: [207, 99]
Point 047: [208, 99]
Point 048: [209, 98]
Point 049: [210, 98]
Point 050: [213, 95]
Point 051: [214, 95]
Point 052: [216, 93]
Point 053: [216, 87]
Point 054: [215, 87]
Point 055: [214, 86]
Point 056: [209, 86]
Point 057: [208, 85]
Point 058: [207, 85]
Point 059: [206, 84]
Point 060: [205, 84]
Point 061: [203, 82]
Point 062: [203, 80]
Point 063: [202, 79]
Point 064: [202, 78]
Point 065: [201, 77]
Point 066: [201, 76]
Point 067: [199, 74]
Point 068: [199, 73]
Point 069: [197, 71]
Point 070: [197, 70]
Point 071: [196, 69]
Point 072: [196, 68]
Point 073: [194, 66]
Point 074: [194, 65]
Point 075: [192, 63]
Point 076: [191, 63]
Point 077: [190, 62]

--- POOL 2 ANALYSIS ---
Precision Points: 58 | Area: 681 px
Point 001: [145, 80]
Point 002: [144, 81]
Point 003: [144, 83]
Point 004: [143, 84]
Point 005: [143, 85]
Point 006: [142, 86]
Point 007: [142, 90]
Point 008: [143, 91]
Point 009: [143, 92]
Point 010: [144, 93]
Point 011: [144, 95]
Point 012: [147, 98]
Point 013: [147, 99]
Point 014: [149, 101]
Point 015: [149, 102]
Point 016: [151, 104]
Point 017: [151, 105]
Point 018: [156, 110]
Point 019: [156, 111]
Point 020: [157, 112]
Point 021: [158, 112]
Point 022: [159, 113]
Point 023: [160, 113]
Point 024: [161, 114]
Point 025: [162, 114]
Point 026: [163, 115]
Point 027: [167, 115]
Point 028: [168, 114]
Point 029: [169, 114]
Point 030: [172, 111]
Point 031: [172, 103]
Point 032: [171, 102]
Point 033: [171, 101]
Point 034: [170, 100]
Point 035: [170, 99]
Point 036: [169, 98]
Point 037: [169, 96]
Point 038: [168, 96]
Point 039: [167, 95]
Point 040: [167, 94]
Point 041: [165, 92]
Point 042: [165, 90]
Point 043: [163, 88]
Point 044: [163, 87]
Point 045: [161, 85]
Point 046: [161, 84]
Point 047: [159, 82]
Point 048: [159, 81]
Point 049: [158, 81]
Point 050: [157, 80]
Point 051: [156, 80]
Point 052: [155, 79]
Point 053: [154, 79]
Point 054: [153, 78]
Point 055: [149, 78]
Point 056: [148, 79]
Point 057: [147, 79]
Point 058: [146, 80]



## Repository Structure

    sanadtech-pool-detection/
    ├── src/
    │   └── pool_detector.py    # Main CLI detection logic
    ├── samples/                # Sample input images for testing
    ├── requirements.txt        # Required Python libraries
    ├── coordinates.txt         # Generated coordinates (last run)
    ├── h.jpg        # Annotated result (last run)
    └── README.md               # Project documentation
