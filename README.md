# SimpleImageConverter

This is a simple image converter application built using Python and the `customtkinter` library. It allows users to select an image file and convert it to different formats such as JPG, WEBP, PNG, BMP, AVIF, and JPEG. The application provides a user-friendly graphical interface for this purpose.

## Features

- Select an image file from your computer.
- Choose the desired output format for the image.
- Convert the selected image to the chosen format.
- Visual feedback on the conversion status.

## Prerequisites

Before you can run the Simple Image Converter, you need to ensure that you have the following components installed:

- Python: The code is written in Python, so you need to have Python installed on your system. You can download it from the [Python website](https://www.python.org/).

- Pillow (PIL Fork): Pillow is a Python Imaging Library that is used for image processing. You can install it using pip:

  ```
  pip install Pillow
  ```

- customtkinter: This is a customized version of the tkinter library for creating graphical user interfaces. It may need to be installed separately based on your system. You can find it on [GitHub](https://github.com/TomSchimansky/CustomTkinter).

## Getting Started

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the project folder.

3. Run the following command to start the Simple Image Converter:

   ```
   python converter.py
   ```

4. The application window will open, allowing you to use the image converter.

## Usage

1. Launch the application.

2. Click the "Select Image" button to choose an image file from your computer. Supported image formats include JPG, JPEG, WEBP, PNG, BMP, AVIF, and more.

3. After selecting an image, the "Output Format" dropdown will display the available image formats for conversion. Choose the desired output format from the dropdown.

4. Click the "Convert" button to initiate the conversion process. The converted image will be saved with the selected format in the same directory as the original image.

5. The application will display a message indicating the successful conversion or prompt you to select an image if one is not selected.

## Custom Icon

The application uses a custom icon for its window. You can change the icon by replacing the `sic.ico` file with your own icon file. Ensure that the icon file is in the `.ico` format.

## Acknowledgments

This Simple Image Converter was created by [0xRezoc](https://github.com/0xRezoc) and is available on GitHub. Feel free to contribute to or modify the code to suit your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

