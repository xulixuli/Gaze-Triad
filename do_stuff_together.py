from files.logger import logger, logger2, logger_run_length

import time
import numpy as np

# class GazeSeq:
#     def __init__(self):
#         self.fsm_states = ['reset','one face','one face one object','one face one object one face']
#         self.state = 'reset'
#         self.obj_indx = 0 #Index of the object that is between two looks on a face
#
#



class DoStuffTogether:

    def __init__(self):
        self.last_frame_index_1 = 0
        self.last_frame_index_2 = 0
        self.prev_state = False
        # self.objects = np.array(["cards", "dice", "key", "map", "phone", "ball"])
        self.objects = np.array(["cards", "dice", "key", "map", "ball", "face"])
        # self.fsm_states = ['reset', 'face', 'face object', 'face object face']
        self.triad_state = 'reset'
        # self.prev_object = 'none'

    def do_some_stuff_together(self, common_data_proxy_1, common_data_proxy_2):
        logger.info("Starting Do_Stuff_Together...")
        # gaze_detect = GazeSeq() #Initialize the object

        while True:
            common_data_1 = common_data_proxy_1.get_values()
            common_data_2 = common_data_proxy_2.get_values()
            if common_data_1[0] is None or common_data_2[0] is None or (
                    common_data_1[2] == self.last_frame_index_1 and common_data_2[2] == self.last_frame_index_2):
                continue

            # logger.info("Glass_1 Frame - {}, Glass_2 Frame - {}, Glass_1 Timestamp - {}, Glass_2 Timestamp - {}".format(
            #     common_data_1[2], common_data_2[2], common_data_1[1], common_data_2[1]))
            # logger.info("Glass_1 output - {}, Glass_2 output - {}".format(common_data_1[3], common_data_2[3]))

            common_look_time = int(time.time() * 1000)
            logger_run_length.info(
                ";time-{};Glass1_hit_scan_output-{};Glass2_hit_scan_output-{};Glass1_run_length_output-{};Glass2_run_length_output-{};Frame1-{};Frame2-{}".format(
                    common_look_time, common_data_1[4], common_data_2[4], common_data_1[3], common_data_2[3], common_data_1[2], common_data_2[2]))

            if common_data_1[3] == common_data_2[3] and sum(common_data_1[3]) != 0:
                if not self.prev_state:
                    self.prev_state = True
                    obj_idx = np.argmax(common_data_1[3])
                    # gaze_status = seq_detect(obj_idx, self.triad_state)
                    # logger2.info("Look Detected;{}:{} Gaze Status {}".format(self.objects[obj_idx], common_look_time, gaze_status))

                    if self.triad_state == 'reset':     # reset
                        if obj_idx == 5:                # + face
                            print("Face Detected")
                            logger2.info("Face Detected;{}:{} ".format(self.objects[obj_idx], common_look_time))
                            self.triad_state = "face"
                            play_sound()
                        else:
                            continue

                    elif self.triad_state == 'face':    # face
                        if obj_idx == 5:                # + face
                            continue
                        else:                           # + object
                            print("Face and Object Detected")
                            logger2.info("Face and Object Detected;{}:{} ".format(self.objects[obj_idx], common_look_time))
                            self.triad_state = 'face_object'
                            play_sound()

                    elif self.state == 'face_object':   # face-object
                        if obj_idx == 5:                # + face
                            print("Gaze Triad Complete")
                            logger2.info("Gaze Triad Complete;{}:{} ".format(self.objects[obj_idx], common_look_time))
                            self.triad_state = 'face'
                            play_sound()
                        # elif object_detected == self.obj_indx:  # + object
                        #     continue
                        else:
                            print("Triad incomplete")
                            logger2.info("Triad incomplete ".format(self.objects[obj_idx], common_look_time))
                            self.triad_state = 'reset'




                # play_sound()
            else:
                self.prev_state = False

            self.last_frame_index_1 = common_data_1[2]
            self.last_frame_index_2 = common_data_2[2]


def play_sound():
    print('\a')

# def seq_detect(object_detected, triad_state):
#     '''
#     The following function keeps track of the objects that are jointly detected
#     And tries to see if a particular sequence of events occur which involves detecting a
#     sequence of three objects starting from a 1) Face 2)Any other Object 3)Face. This is
#     defined as a gaze traid.
#     Inputs and Constraints:
#     object_detected: Is an integer which has the information of what object is present in the detection
#     also referred to as obj_indx at parent function
#     Output: True if such sequence of event occured else False
#     '''
#     assert isinstance(object_detected, int)
#     assert object_detected < 6 and object_detected >= 0
#
#     # initailization #Assume Face 1



    
    
    

