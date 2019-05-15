
import tensorflow as tf
import csv
import cv2
import numpy as np
from utils import visualization_utils as vis_util
import random
import time
from uuid import uuid4
import os

# Variables
total_passed_vehicle = 0  # using it to count vehicles

# 

def targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_object, fps, width, height):
        #initialize .csv
        # input video

        cap = cv2.VideoCapture(input_video)
        width_heigh_taken = True
        height = 0
        width = 0
        with detection_graph.as_default():
          with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            # for all the frames that are extracted from input video
            while(cap.isOpened()):
                ret, image_np = cap.read()                

                if not  ret:
                    print("end of the video file...")
                    break
                random_time = random.randrange(10,20)
                # time.sleep(random_time)
                # ts = time.time()
                input_frame = image_np

                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                # insert information text to video frame
                font = cv2.FONT_HERSHEY_SIMPLEX

                # Visualization of the results of a detection.        
                counter, csv_line, the_result = vis_util.visualize_boxes_and_labels_on_image_array(cap.get(1),
                                                                                                      input_frame,
                                                                                                      1,
                                                                                                      is_color_recognition_enabled,
                                                                                                      np.squeeze(boxes),
                                                                                                      np.squeeze(classes).astype(np.int32),
                                                                                                      np.squeeze(scores),
                                                                                                      category_index,
                                                                                                      targeted_objects=targeted_object,
                                                                                                      use_normalized_coordinates=True,
                                                                                                      line_thickness=4)
                if(len(the_result) == 0):
                    cv2.putText(input_frame, "Does not match target", (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)                       
                
                else:
                    # print(the_result)
                    with open('object_counting_report.csv', 'w') as f:
                            writer = csv.writer(f)  
                            # res = [str(objects) for obj in the_result]
                            result = the_result
                            csv_line = result
                            writer.writerows([csv_line.split(';')])
                    # with open('object_counting_report.csv', 'r') as f:
                    #         writer = csv.reader(f)  
                    #         for line in writer:
                                # line2= [l.split(':') for l in line]
                                
                                # line2[line2.index(":")] = ''
                                # print(line)
                    cv2.putText(input_frame, the_result, (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)
                
                cv2.imshow('object counting',input_frame)

                print ("writing frame")
                # os.remove(file) for file in os.listdir('fridge_screenshots') if file.endswith('.png')
                try: 
                    os.remove("static/images/fridge_screenshots/your_fridge.png")
                except: pass
                # cv2.imshow('img1',image_np) #display the captured image
                outfile = 'fridge_screenshots/your_fridge.jpg'

                cv2.imwrite(outfile,image_np)
                # print ("Next picture in: %.2f minutes" % (float(random_time) / 60))

                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                # if(csv_line != "not_available"):
                #         with open('d.csv', 'a') as f:
                #                 writer = csv.writer(f)                          
                #                 size, direction = csv_line.split(',')                                             
                #                 writer.writerows([csv_line.split(',')])         
            #         #initialize .csv
            # with open('object_counting_report.txt', 'w') as f:
            #         writer = csv.writer(f)  
            #         csv_line = "Object Type, Object Color, Object Movement Direction, Object Speed (km/h)"          
            #         writer.writerows([csv_line.split(',')])
            # with open('object_counting_report.txt', 'r') as f:
            #         writer = csv.reader(f)  
            #         for line in writer:
            #             print(line)
            #             print('ghjkjhgfdfghjk')                                                                                 

            cap.release()
            cv2.destroyAllWindows()

def object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, fps, width, height):
        #initialize .csv
        with open('grocery_report.csv', 'w') as f:
                writer = csv.writer(f)  
                csv_line = "Grocery, Qty"                 
                writer.writerows([csv_line.split(',')])


        # input video
        cap = cv2.VideoCapture(input_video)

        counting_mode = "..."
        height = 0
        width = 0
        with detection_graph.as_default():
          with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
     
            
            while True:
                ret, image_np = cap.read()         

                if not  ret:
                    print("end of the video file...")
                    break
                
                input_frame = image_np

                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                # insert information text to video frame
                font = cv2.FONT_HERSHEY_SIMPLEX

                # Visualization of the results of a detection.        
                counter, csv_line, counting_mode = vis_util.visualize_boxes_and_labels_on_image_array(cap.get(0),
                                                                                                      input_frame,
                                                                                                      1,
                                                                                                      is_color_recognition_enabled,
                                                                                                      np.squeeze(boxes),
                                                                                                      np.squeeze(classes).astype(np.int32),
                                                                                                      np.squeeze(scores),
                                                                                                      category_index,
                                                                                                      use_normalized_coordinates=True,
                                                                                                  line_thickness=4)
                # counting_mode = counting_mode + counter
                # print (counting_mode)

                if(len(counting_mode) == 0):
                    cv2.putText(input_frame, "...", (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)                       
                else:
                    cv2.putText(input_frame, str(counting_mode), (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)
                
                

                # print ("writing frame")
                cv2.imshow('grocery counting',input_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                if(counting_mode != "..."):
                    with open('grocery_r.csv', 'w') as f:
                        writer = csv.writer(f)                          
                        # size, direction = csv_line.split(',')                                             
                        # writer.writerows([csv_line.split(',')])  
                    # with open('grocery_r.csv' ,'r') as reading:
                    #     read = csv.reader(reading)
                    #     for line in read:
                            # line2 = 
                            # print(line)        
                                   

            cap.release()
            cv2.destroyAllWindows()