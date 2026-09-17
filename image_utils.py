import cv2
import os


def load_image(filename):
    image = cv2.imread(filename)

    if image is None:
        raise FileNotFoundError(
            f"Could not find or open the image: {filename}"
        )

    return image


def create_output_folder():
    os.makedirs("output", exist_ok=True)


def save_image(image, filename):
    create_output_folder()
    output_path = os.path.join("output", filename)

    success = cv2.imwrite(output_path, image)

    if not success:
        raise IOError(f"Could not save image: {output_path}")

    return output_path