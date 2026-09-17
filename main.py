from image_utils import load_image, save_image
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


def display_menu():
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


def main():
    try:
        image = load_image("input.jpg")

        display_menu()

        choice = int(input("\nEnter your choice: "))

        transformations = {
            1: (brightness, "brightness.jpg"),
            2: (contrast, "contrast.jpg"),
            3: (negative, "negative.jpg"),
            4: (gamma_transformation, "gamma.jpg"),
            5: (thresholding, "threshold.jpg"),
            6: (translation, "translation.jpg"),
            7: (scaling, "scaling.jpg"),
            8: (rotation, "rotation.jpg"),
            9: (horizontal_reflection, "horizontal_reflection.jpg"),
            10: (vertical_reflection, "vertical_reflection.jpg"),
            11: (x_shearing, "x_shear.jpg"),
            12: (y_shearing, "y_shear.jpg"),
            13: (affine_transformation, "affine.jpg")
        }

        if choice not in transformations:
            print("Invalid choice. Please select a number from 1 to 13.")
            return

        transformation_function, filename = transformations[choice]

        result = transformation_function(image)

        output_path = save_image(result, filename)

        print("\nTransformation completed successfully!")
        print(f"Output saved in: {output_path}")

    except ValueError:
        print("Error: Please enter a valid number.")

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()