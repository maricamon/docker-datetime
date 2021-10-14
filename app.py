from flask import Flask, request, jsonify
import arrow

app = Flask(__name__)

@app.route('/')
def datetime():
  payload = request.get_json(force=True)
  timezone = payload["timezone"]
  utc =  arrow.utcnow()
  try:
    local = utc.to(timezone)
    dtime = local.format('YYYY-MM-DD HH:mm:ss')
    return jsonify({"datetime": dtime})
  except:
    return jsonify("Invalid timezone")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
