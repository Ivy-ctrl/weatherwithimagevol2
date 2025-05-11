from flask import Flask, render_template, request
from tester import get_weather_and_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inputinfo3.html')

@app.route('/getweather', methods=['POST'])
def getweather():
    city = request.form['city']
    weather_data, image_url = get_weather_and_image(city)

    return render_template('outputinfo3.html', city=city, weather=weather_data, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
