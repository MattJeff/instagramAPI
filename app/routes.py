from flask import Blueprint, request, jsonify
from .utils import authenticate_instaloader, get_instagram_user_info, get_script_video_url
import os
import logging

main = Blueprint('main', __name__)

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
    logging.error("Instagram username or password not set in environment variables")

@main.route('/get_instagram_user_info', methods=['POST'])
def get_instagram_user_info_endpoint():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    try:
        L = authenticate_instaloader(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        user_info = get_instagram_user_info(username, L)
        return jsonify(user_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/get_script_video_url', methods=['POST'])
def get_script_video_url_endpoint():
    data = request.get_json()
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({'error': 'Video URL is required'}), 400
    
    try:
        L = authenticate_instaloader(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        video_info = get_script_video_url(video_url, L)
        return jsonify(video_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/', methods=['GET'])
def test_endpoint():
    return jsonify({'message': 'The application is working correctly!'})
