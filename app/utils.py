import instaloader
import whisper
import requests
import os
import logging

logging.basicConfig(level=logging.INFO)

def authenticate_instaloader(username, password, session_file='session'):
    L = instaloader.Instaloader()
    if os.path.exists(session_file):
        logging.info('Loading session from file...')
        L.load_session_from_file(username, session_file)
    else:
        try:
            logging.info('Logging in...')
            L.login(username, password)
            L.save_session_to_file(session_file)
        except instaloader.exceptions.CheckpointRequiredException as e:
            logging.error(f'Login error: {e}. Please complete the checkpoint verification in your browser.')
            raise
    return L

def get_instagram_user_info(username, L):
    profile = instaloader.Profile.from_username(L.context, username)
    
    user_info = {
        'username': profile.username,
        'num_posts': profile.mediacount,
        'num_followers': profile.followers,
        'num_following': profile.followees,
        'profile_pic_url': profile.profile_pic_url
    }
    
    return user_info

def get_script_video_url(video_url, L):
    shortcode = video_url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    
    video_info = {
        'upload_date': post.date.strftime('%Y-%m-%d %H:%M:%S'),
        'num_likes': post.likes,
        'num_views':post.video_view_count,
        'num_comments': post.comments,
        'creator': post.owner_username,
        'cover_image_url': post.url,
        'video_url': post.video_url
    }

    model = whisper.load_model("base")
    video_response = requests.get(post.video_url, verify=False)
    with open('temp_video.mp4', 'wb') as f:
        f.write(video_response.content)
    
    result = model.transcribe('temp_video.mp4')
    video_info['transcript'] = result['text']
    
    return video_info
