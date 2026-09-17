import cv2
import numpy as np
import os

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found.")
    exit()

# Create output folder
os.makedirs("output", exist_ok=True)

print("\n===== COMPUTER VISION IMAGE TRANSFORMATION TOOL =====")
print("1. Brightness")
print("2. Contrast")
print("3. Negative")
print("4. Gamma Transformation")
print("5. Thresholding")
print("6. Translation")
print("7. Scaling")
print("8. Rotation")
print("9. Horizontal Reflection")
print("10. Vertical Reflection")
print("11. X-axis Shearing")
print("12. Y-axis Shearing")
print("13. Affine Transformation")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    result = cv2.convertScaleAbs(image, alpha=1.0, beta=50)
    name = "brightness.jpg"

elif choice == 2:
    result = cv2.convertScaleAbs(image, alpha=1.8, beta=0)
    name = "contrast.jpg"

elif choice == 3:
    result = 255 - image
    name = "negative.jpg"

elif choice == 4:
    gamma = 2.0
    table = np.array(
        [((i / 255.0) ** gamma) * 255 for i in np.arange(256)]
    ).astype("uint8")
    result = cv2.LUT(image, table)
    name = "gamma.jpg"

elif choice == 5:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    name = "threshold.jpg"

elif choice == 6:
    matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    result = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    name = "translation.jpg"

elif choice == 7:
    result = cv2.resize(image, None, fx=1.5, fy=1.5)
    name = "scaling.jpg"

elif choice == 8:
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    result = cv2.warpAffine(image, matrix, (width, height))
    name = "rotation.jpg"

elif choice == 9:
    result = cv2.flip(image, 1)
    name = "horizontal_reflection.jpg"

elif choice == 10:
    result = cv2.flip(image, 0)
    name = "vertical_reflection.jpg"

elif choice == 11:
    height, width = image.shape[:2]
    matrix = np.float32([[1, 0.4, 0], [0, 1, 0]])
    result = cv2.warpAffine(image, matrix, (width, height))
    name = "x_shear.jpg"

elif choice == 12:
    height, width = image.shape[:2]
    matrix = np.float32([[1, 0, 0], [0.4, 1, 0]])
    result = cv2.warpAffine(image, matrix, (width, height))
    name = "y_shear.jpg"

elif choice == 13:
    source = np.float32([[50, 50], [200, 50], [50, 200]])
    destination = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix = cv2.getAffineTransform(source, destination)

    height, width = image.shape[:2]
    result = cv2.warpAffine(image, matrix, (width, height))
    name = "affine.jpg"

else:
    print("Invalid choice.")
    exit()

cv2.imwrite("output/" + name, result)

print("\nTransformation completed successfully!")
print("Output saved in: output/" + name)