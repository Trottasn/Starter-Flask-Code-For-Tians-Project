from flask import Flask, stream_with_context, Response
app = Flask(__name__)

@app.route('/stream_data')
def stream_data():
    def generate():
        with open("./videos/test.mp4", "rb") as f:
            while True:
                chunk = f.read(1024)
                if chunk:
                    yield chunk
                else:
                    break

    return Response(stream_with_context(generate()), mimetype="video/mp4")

if __name__ == "__main__":
    app.run()
