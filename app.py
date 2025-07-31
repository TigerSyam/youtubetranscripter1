from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    vid = request.args.get('id')
    if not vid:
        return jsonify({'error': 'Missing video ID'}), 400
    try:
        ytt_api = YouTubeTranscriptApi()
        data =ytt_api.fetch(vid,preserve_formatting=True)
        text = " ".join([e['text'] for e in data])
        return jsonify({'transcript': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
