from flask import *
from utilities.kafka.producer_test import send_messages
from flask import  jsonify, request
from utilities.kafka.producer_test import send_messages
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/pushtotopic", methods=['GET'])
def push_to_topic():
    try:
        data = request.json['data']
        send_messages(data)
        return jsonify({"status": "success", "message": "successfully pushed to the topic"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

"""
./zookeeper-server-start.sh ../config/zookeeper.properties
./kafka_dependency-server-start.sh ../config/server.properties
 ./kafka_dependency-topics.sh --bootstrap-server aryan-Swift-SF314-55G:9092 --create --topic testtopic --partitions 1 --replication-factor 1
"""
