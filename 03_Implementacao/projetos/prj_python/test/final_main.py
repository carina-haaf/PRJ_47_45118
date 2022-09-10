from additional.constants import *
import generateTestVideoDataset
import generateVideoMiniClips

print("- Generating dataset for " + TEST_VIDEO_NAME + "...")
generateTestVideoDataset.generate_video_dataset()

print("\n\nVideo classification with loaded model and video mini-clips generation...")
generateVideoMiniClips.generate()

print("\n\n\nNext steps: ")
print("1. Open 'test/mini_clips/' directory")
print("2. Copy the LAST directory created to the directory 'videos' inside 'padelApp' project")
print("3. Run 'padelApp' project")
