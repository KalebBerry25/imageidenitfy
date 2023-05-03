# imageidentify
### Install imageidentify from PyPi.
```bash
pip install imageidentify
```
Example
-------
>>> # Import library
>>> from imageidentify import imageidentify
>>> # Initialize
>>> prediction = identify(image_path)
>>> # Print description
>>> print(final_description(prediction))

imageidentify is a python package that can be used to output a simple description  of the objects an image contains using the Inception_V3 ImageNet model.
