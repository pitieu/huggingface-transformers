import json
from flask import Flask, request
from lib.predictor import ImagePredictor
from lib.predictor2 import ImagePredictor2
from lib.timer import Timer

app = Flask(__name__)

@app.route("/tag")
def hello():
    image_name = request.args.get('imageName')
    if not image_name:
      return "Error: No image name provided."
    
    Timer.start()
    predictor = ImagePredictor()
    image_path = f'./assets/{image_name}.jpg'
    result = predictor.predict([image_path])
    Timer.end()
    response = {
        "output": result[0],
        "execution_time": Timer.execution_time
    }
    return json.dumps(response)

@app.route("/tag2")
def hello2():
    image_name = request.args.get('imageName')
    if not image_name:
      return "Error: No image name provided."
    
    Timer.start()
    predictor = ImagePredictor2()
    image_path = f'./assets/{image_name}.jpg'
    result = predictor.predict([image_path])
    Timer.end()
    response = {
        "output": result[0],
        "execution_time": Timer.execution_time
    }
    return json.dumps(response)

Timer.start()
predictor = ImagePredictor2()
image_path = f'./assets/3.jpg'
result = predictor.predict([image_path])
Timer.end()
print("Execution time", Timer.execution_time)
print(result)

if __name__ == "__main__":
    app.run(port=8001)

