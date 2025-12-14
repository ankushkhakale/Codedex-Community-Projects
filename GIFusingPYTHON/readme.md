# GIF Generator using Python

This project is a simple Python script that creates an animated GIF from a set of static images. It uses the `imageio` library to seamlessy stitch images together into a looping animation.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.5+**: The script requires Python installed on your system.
- **imageio**: This library is used for reading and writing image data.

## Installation

1.  **Clone the repository** (if applicable) or download the project files.
2.  **Install the required library**:
    Open your terminal or command prompt and run the following command to install `imageio`:

    ```bash
    pip install imageio
    ```

## Usage

1.  Ensure you have your images named `codedex1.jpg` and `codedex2.jpg` in the same directory as the script. (You can modify the `filenames` list in the script to use different images).
2.  Run the Python script:

    ```bash
    python create_gif.py
    ```

3.  After the script runs successfully, a new file named `codedex.gif` will be created in the directory.

## How it Works

The script `create_gif.py` performs the following steps:
1.  Imports the `imageio` library.
2.  Defines a list of image filenames (`codedex1.jpg`, `codedex2.jpg`).
3.  Reads each image file and stores the data.
4.  Writes the collected image data into a single GIF file (`codedex.gif`) with a specified duration for each frame (0.5 seconds) and sets it to infinite loop.
