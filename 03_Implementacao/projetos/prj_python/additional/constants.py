from datetime import datetime
import numpy as np
import os

# CONSTANTS

# chose classifier / model on test process
EXPERIMENT = 12
CHOSE_MODEL = 3  # to test models created on CV training process
CV_MODE = False  # whether it is training with alla data (False) or with cross validation (True)
LABELS = False


# time hyper parameters
NOG = 5  # number of groups
SPG = 4096  # samples per group
NOF = 3  # number of features
NOSS = 4096  # number of shifted samples


# NN hyper parameters
LR = 0.001  # learning rate
NR_EPOCHS = 100
BATCH_SIZE = 128
LOSS_FUNCTION = "binary_crossentropy"  # "binary_crossentropy"
DECISION_LIMIT = 0.5  # to decide whether it is a ball hit or noise
NR_OF_INPUT_LAYER_NODES = NOG * NOF
OUTPUT_ACTIVATION_FUNCTION = "sigmoid"
HIDDEN_LAYERS_ACTIVATION_FUNCTION = "relu"


# Cross validation
NR_KFOLDS = 5


# directories path
AUDIOS_PATH = "../../data/audios"
VIDEOS_PATH = "../../data/videos"
TRAINED_MODELS_PATH = "trained_models/constructed_models"
TRAINED_MODELS_GRAPHS_PATH = "trained_models/models_graphs"
TRAINED_MODELS_WITH_ALL_DATA_PATH = "trained_models/trained_models_with_all_data"

TEST_VIDEO_PATH = "./test_videos"
TEST_AUDIO_PATH = "./test_audios"
TEST_DIR_PATH = "test"
MODEL_PATH = "model"

# files path
ODM_DATASET_PATH = "../data/odm_features_file.csv"
MAIN_DATASET_PATH = "data/features_file.csv"
TEST_DATASET_PATH = "features_test_file.csv"
LABELING_FILES_PATH = "../data/labeling"
LABELING_TEST_FILES_PATH = "dataset/data/labeling"


# test video name
TEST_VIDEO_NAME = files = np.array(list(os.listdir("test_videos")))[0]
MINI_CLIPS_VIDEO_NAME = "vid_" + datetime.today().strftime('%d_%m_%Y_%H_%M_%S')

MINI_CLIPS_VIDEO_NAME_PATH = "mini_clips/" + MINI_CLIPS_VIDEO_NAME
MINI_CLIPS_INFO_PATH_TO_REMOVE = MINI_CLIPS_VIDEO_NAME_PATH + "/clips_info.txt"
MINI_CLIPS_INFO_PATH_TO_CREATE = "test/" + MINI_CLIPS_VIDEO_NAME_PATH + "/clips_info.txt"
DATASET_CLASSES_PATH_TO_REMOVE = MINI_CLIPS_VIDEO_NAME_PATH + "/dataset/dataset_classes.txt"
DATASET_CLASSES_PATH_TO_CREATE = "test/" + MINI_CLIPS_VIDEO_NAME_PATH + "/dataset/dataset_classes.txt"
MINI_CLIPS_INFO_NON_SORTED_PATH_TO_REMOVE = "test/" + MINI_CLIPS_VIDEO_NAME_PATH + "/clips_info_non_sorted.txt"
MINI_CLIPS_INFO_NON_SORTED_PATH_TO_CREATE = "test/" + MINI_CLIPS_VIDEO_NAME_PATH + "/clips_info_non_sorted.txt"
README_TO_REMOVE = MINI_CLIPS_VIDEO_NAME_PATH + "/readme.txt"
README_TO_CREATE = "test/" + MINI_CLIPS_VIDEO_NAME_PATH + "/readme.txt"
