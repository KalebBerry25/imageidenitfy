from imageidentify.imageidentify import identify_image, final_description

__author__ = 'D.Quadri and K.Berry'
__email__ = 'damola.quadri@bison.howard.edu and kaleb.berry@bison.howard.edu'
__version__ = '0.1.0'

# module level doc-string
__doc__ = """
imageidentify
=============

Description
-----------
imageidentify is a python package that can be used to output a simple description 
of the objects an image contains using the Inception_V3 ImageNet model.

Example
-------
>>> # Import library
>>> from imageidentify.imageidentify import identify_image, final_description
>>> # Initialize
>>> prediction = identify(image_path)
>>> # Print description
>>> print(final_description(prediction))


References
----------
* https://www.tensorflow.org/api_docs/python/tf/keras/applications/inception_v3/InceptionV3

"""