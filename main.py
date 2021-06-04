from flask import Flask, render_template
from aero import get_igc_header

app = Flask(__name__)


@app.route('/')
def index():
    info = get_igc_header()
    return render_template('index.html',
                           pilot_name=info['pilot'],
                           glider_model=info['glider_model'],
                           competition_id=info['competition_id']
                           )


if __name__ == '__main__':
    app.run()
