
from PIL import Image

def read_file(filepath):
    """
    Read file at file path and return a matrix. Each pixel is represented by a list of 3 integers
    representing the red, green and blue scale.

    For instance, imagine you have a 3x2 black and white image that
    makes a "V" shape. This code would return:

    [ [[255, 255, 255], [  0,   0,   0], [255, 255, 255]],
      [   0,   0,   0], [255, 255, 255], [  0,   0,   0]]

    PIL defaults to making the Coordinate system where the
    horizontal is the first dimension and the vertial is the second
    dimension. Source: https://pillow.readthedocs.io/en/latest
    /handbook/concepts.html#coordinate-system.
    """
    image = Image.open(filepath)
    img_data = image.getdata()
    return [[list(img_data.getpixel((x, y))[:3]) for x in range(image.width)] for y in range(image.height)]

def write_to_file(filepath, image_matrix, img_format="png"):
    """
    Write an image matrix to a file. The image matrix must be made of lists with 3 entries.

    Parameters:
    filepath: {str} The relative path to the file to write to.
    image_matrix: {list of lists of lists} Matrix to write.
    img_format: {str} Optional. Type of file to save as. jpg also
    supported.

    Does not return anything.
    """
    if not image_matrix or not image_matrix[0]:
        raise ValueError("Cannot write image matrix with 0 width or height")

    image = Image.new(
        mode="RGB",
        size=(len(image_matrix[0]), len(image_matrix)))

    for row_index, _ in enumerate(image_matrix[0]):
        for col_index, _ in enumerate(image_matrix):
            pixel = tuple(image_matrix[col_index][row_index])
            image.putpixel((row_index, col_index), pixel)

    image.save(filepath, img_format)
