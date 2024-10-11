from moviepy.editor import TextClip, concatenate_videoclips

def text_to_movie(text_file, output_path, clip_duration=5):
    with open(text_file, 'r') as file:
        lines = file.readlines()

    clips = []
    for line in lines:
        clip = TextClip(line.strip(), fontsize=70, color='white', bg_color='black').set_duration(clip_duration)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_path, fps=24)

# Example usage
text_file = "example_text.txt"
output_movie_path = "movie.mp4"
text_to_movie(text_file, output_movie_path)
