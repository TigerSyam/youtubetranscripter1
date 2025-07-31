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
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env variable
    app.run(host='0.0.0.0', port=port)
