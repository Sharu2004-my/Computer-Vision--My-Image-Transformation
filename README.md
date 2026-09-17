# Computer Vision Image Transformation Tool

## Project Description

This project is a Python-based Computer Vision Image Transformation Tool developed using OpenCV and NumPy.

It allows the user to apply different image transformations such as:

* Brightness adjustment
* Contrast adjustment
* Negative transformation
* Gamma transformation
* Thresholding
* Translation
* Scaling
* Rotation
* Horizontal reflection
* Vertical reflection
* X-axis shearing
* Y-axis shearing
* Affine transformation

## Requirements

* Python 3.x
* OpenCV
* NumPy

## Installation

Install the required Python libraries using:

```bash
pip install opencv-python numpy
```

## Input Image

Place an image named `input.jpg` in the same folder as the Python program.

## How to Run

Open a terminal in the project folder and run:

```bash
main.py<img width="1204" height="1600" alt="input" src="https://github.com/user-attachments/assets/a36bbf71-6334-40da-b836-7b9217d031e0" />
[main.py](https://github.com/user-attachments/files/32340946/main.py)

```

The program will display a menu of available transformations.

Enter the number corresponding to the transformation you want to apply.

For example:

```text
Enter your choice: 1
```

The selected transformation will be applied to `input.jpg`.

## Output

The transformed image will be saved automatically inside the `output` folder.

For example:

```text
output/brightness.jpg
```

The `output` folder is created automatically by the program if it does not already exist.

## Project Structure

```text
Computer-Vision--My-Image-Transformation/
│
├── README.md
├── image_transformation.py
├── input.jpg
└── output/
```

## Technologies Used

* Python
* OpenCV
* NumPy
