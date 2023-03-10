# add the video to this video clip
from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


def extract_video_clip(file_name, time_start, time_end, file_path):
    """ file_path: this is where i am saving the new video """

    # Returns the location of the video created
    clip = VideoFileClip(file_name)
    # Specify the start and end times for the edited clip
    edited_clip = clip.subclip(time_start, time_end)
    # Save the edited clip to a new file
    edited_clip.write_videofile(file_path,
                                codec="h264",
                                bitrate="5000k",
                                threads=4,
                                preset="medium")
    return file_path


def merge_all_videos(video_clipped_list: list, folder_name):
    """
    This merges all videos in a list base on their order and the list contains
    instance of [VideoFileClip(file),VideoFileClip(file)]
    :return: None
    """
    # concatenating both the clips
    # Get the first clip frame per second
    fps = video_clipped_list[0].fps
    final = concatenate_videoclips(video_clipped_list, method="compose")
    # writing the video into a file / saving the combined video
    final.write_videofile(f"{folder_name}/merged_{folder_name}.mp4", codec="h264",
                          bitrate="5000k",
                          threads=4,
                          preset="medium", fps=fps)
