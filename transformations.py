import cv2
import numpy as np
import config


def brightness(image):
    return cv2.convertScaleAbs(
        image,
        alpha=1.0,
        beta=config.BRIGHTNESS_VALUE
    )


def contrast(image):
    return cv2.convertScaleAbs(
        image,
        alpha=config.CONTRAST_VALUE,
        beta=0
    )


def negative(image):
    return 255 - image


def gamma_transformation(image):
    gamma = config.GAMMA_VALUE

    table = np.array(
        [((i / 255.0) ** gamma) * 255 for i in np.arange(256)]
    ).astype("uint8")

    return cv2.LUT(image, table)


def thresholding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, result = cv2.threshold(
        gray,
        config.THRESHOLD_VALUE,
        255,
        cv2.THRESH_BINARY
    )

    return result


def translation(image):
    matrix = np.float32([
        [1, 0, config.TRANSLATION_X],
        [0, 1, config.TRANSLATION_Y]
    ])

    height, width = image.shape[:2]

    return cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )


def scaling(image):
    return cv2.resize(
        image,
        None,
        fx=config.SCALE_X,
        fy=config.SCALE_Y
    )


def rotation(image):
    height, width = image.shape[:2]

    center = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(
        center,
        config.ROTATION_ANGLE,
        1.0
    )

    return cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )


def horizontal_reflection(image):
    return cv2.flip(image, 1)


def vertical_reflection(image):
    return cv2.flip(image, 0)


def x_shearing(image):
    height, width = image.shape[:2]

    matrix = np.float32([
        [1, config.SHEAR_X, 0],
        [0, 1, 0]
    ])

    return cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )


def y_shearing(image):
    height, width = image.shape[:2]

    matrix = np.float32([
        [1, 0, 0],
        [config.SHEAR_Y, 1, 0]
    ])

    return cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )


def affine_transformation(image):
    source = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    destination = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    matrix = cv2.getAffineTransform(
        source,
        destination
    )

    height, width = image.shape[:2]

    return cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )