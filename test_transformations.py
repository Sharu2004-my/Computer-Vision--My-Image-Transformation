import cv2

from image_utils import load_image
from transformations import (
    brightness,
    contrast,
    negative,
    gamma_transformation,
    thresholding,
    translation,
    scaling,
    rotation,
    horizontal_reflection,
    vertical_reflection,
    x_shearing,
    y_shearing,
    affine_transformation
)


def test_transformations():
    image = load_image("input.jpg")

    results = [
        brightness(image),
        contrast(image),
        negative(image),
        gamma_transformation(image),
        thresholding(image),
        translation(image),
        scaling(image),
        rotation(image),
        horizontal_reflection(image),
        vertical_reflection(image),
        x_shearing(image),
        y_shearing(image),
        affine_transformation(image)
    ]

    for result in results:
        assert result is not None
        assert result.size > 0

    print("All transformation tests passed successfully!")


if __name__ == "__main__":
    test_transformations()