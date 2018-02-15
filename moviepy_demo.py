from moviepy.editor import *
import os, sys, time

dur_time = 2.5
fps = 1

files = [
    { 'type': 'vid', 'p': 'VID_20180215_114739104.mp4', 'sub': [0,3], 't': "drilling holes" },
    { 'type': 'vid', 'p': 'VID_20180215_115249782.mp4', 'sub': [0,3], 't': "milling outline" },
    { 'type': 'img', 'p': 'IMG_20180215_115620141.jpg', 'd': dur_time, 't': "filing edges to ensure flatness" },
    { 'type': 'img', 'p': 'IMG_20180215_115751222.jpg', 'd': dur_time, 't': "aligning printed mask over pcb" },
    { 'type': 'img', 'p': 'IMG_20180215_115819622.jpg', 'd': dur_time, 't': "exposure with UV light (2mins)" },
    { 'type': 'img', 'p': 'IMG_20180215_120413522.jpg', 'd': dur_time, 't': "second layer" },
    { 'type': 'img', 'p': 'IMG_20180215_121654160.jpg', 'd': dur_time, 't': "etch tank settings" },
    { 'type': 'img', 'p': 'TEMPS.jpg', 'd': dur_time, 't': "tank temperatures" },
    { 'type': 'vid', 'p': 'VID_20180215_121002216.mp4', 'sub': [0,3], 't': "developing" },
    { 'type': 'vid', 'p': 'VID_20180215_121558366.mp4', 'sub': [0,5], 't': "after development" },
    { 'type': 'img', 'p': 'IMG_20180215_122933733.jpg', 'd': dur_time, 't': "check etch start" },
    { 'type': 'img', 'p': 'IMG_20180215_124125567.jpg', 'd': dur_time, 't': "etch finished, remove mask with IPA" },
    { 'type': 'vid', 'p': 'VID_20180215_124238520.mp4', 'sub': [13,17], 't': "after etching" },
    { 'type': 'img', 'p': 'IMG_20180215_124610229.jpg', 'd': dur_time, 't': "inspection" },
    { 'type': 'img', 'p': 'IMG_20180215_130549468.jpg', 'd': dur_time, 't': "test first set of leds" },
    { 'type': 'img', 'p': 'IMG_20180215_131929574.jpg', 'd': dur_time, 't': "leds soldered" },
    { 'type': 'img', 'p': 'IMG_20180215_132033655.jpg', 'd': dur_time, 't': "start soldering vias" },
    { 'type': 'img', 'p': 'IMG_20180215_134141036.jpg', 'd': dur_time, 't': "test blue leds" },
    { 'type': 'img', 'p': 'IMG_20180215_134825801.jpg', 'd': dur_time, 't': "... green leds ..." },
    { 'type': 'vid', 'p': 'VID_20180215_135111338.mp4', 'sub': [0,8], 't': "fade led test" },
    { 'type': 'vid', 'p': 'VID_20180215_141811433.mp4', 'sub': [5,16], 't': "blue, green & blue and green" },
]

clips_with_text = []
image_width = None 
try:
    for clip in files:
        print(clip)
        if clip['type'] == 'vid':
            video = VideoFileClip('./media/' + clip['p'])
            if clip['sub'] is not None:
                video = video.subclip(*clip['sub'])
        elif clip['type'] == 'img':
            video = ImageClip('./media/' + clip['p'], duration=clip['d']).set_fps(fps)
            if image_width is None:
                image_width = video.w
            else:
                if video.w != image_width:
                    exit("image must be same size as previously used ones: %d" % image_width)
            video = video.resize(0.5) # make the video smaller as the images are big

        txt_clip = TextClip(clip['t'], fontsize=120, color='white', bg_color='black', font='Liberation-Sans-Bold').set_position(("center", "bottom")).set_duration(video.duration)

        result = CompositeVideoClip([video, txt_clip]) # Overlay text on video

        clips_with_text.append(result)

    final_clip = concatenate_videoclips(clips_with_text)
    print(final_clip.w, final_clip.h)
    final_clip = final_clip.resize(0.5)
    print(final_clip.w, final_clip.h)
    final_clip.write_videofile("final.py3.mp4", audio=False)

except Exception as e:
    print(e)
    import ipdb; ipdb.set_trace()
