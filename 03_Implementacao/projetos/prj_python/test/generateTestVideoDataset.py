
# TESTE SOBRE UM VIDEOO NOVO PARA PROCESSO DE CONSTRUÇÃO DAS PASTAS A SEREM USADAS
# NA VISUALIZAÇÃO DOS RESULTADOS

# =================================================================================
# Imports ...
# =================================================================================
import testDatasetConstructor
import testDatasetConstructorWithoutLabels
from additional.videoProcessing import *
from additional.constants import *
from additional.processCsvFile import *
from additional.directoryManipulator import *
import testDatasetConstructor


# =================================================================================
# generate dataset from new/test data...
# =================================================================================


def generate_video_dataset():

    # hyper parameters
    nog = NOG  # number of groups
    spr = SPG  # samples per group
    nof = NOF  # number of features
    noss = NOSS  # number of shifted samples

    clear_dir(TEST_AUDIO_PATH)

    file_rows = list()

    CsvFile.remove_file("../" + TEST_DIR_PATH + "/" + TEST_DATASET_PATH)
    features_file = CsvFile(TEST_DIR_PATH + "/" + TEST_DATASET_PATH, "w")

    paths_train = [TEST_VIDEO_PATH, TEST_AUDIO_PATH]

    # make sure that the 'test/test_videos' directory have just ONE video
    if len(np.array(list(os.listdir("test_videos")))) > 1:
        print("Directory 'test/test_videos' CAN ONLY HAVE one video.")
        exit(0)

    # in constants.py change LABELS value to "True" in case you want Supervised classification
    if LABELS:
        testDatasetConstructor.construct(paths_train, nog, spr,
                                         noss, features_file, file_rows)
    else:
        testDatasetConstructorWithoutLabels.construct(paths_train, nog, spr,
                                                      noss, features_file, file_rows)


if __name__ == "__main__":
    generate_video_dataset()
