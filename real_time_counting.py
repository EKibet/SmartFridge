# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting_api


# if tf.__version__ < '1.11.0':
#   raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')

input_video = 0

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('faster_rcnn_inception_v2_coco_2018_01_28')

#object_counting_api.object_counting(input_video, detection_graph, category_index, 0) # for counting all the objects, disabled color prediction

# object_counting_api.object_counting(input_video, detection_graph, category_index, 1) # for counting all the objects, enabled color prediction


fps = 24 # change it with your input video fps
width = 954 # change it with your input video width
height = 580 # change it with your input vide height
is_color_recognition_enabled = 0


object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, fps, width, height) # counting all the objects
