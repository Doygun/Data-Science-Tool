# coding=utf-8
"""

Data Cleaning
"""
__author__ = 'Seray Beser'


class PreprocessService(object):
    """
    Preprocess Service

    Basic Usage:

    >> preprocess_service_ = PreprocessService(preprocess_name='Cleaning')
    """

    def __init__(self, preprocess_name=None):
        self.name = preprocess_name
