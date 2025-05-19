from flask import Flask, jsonify

from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'sso-svc-prod',

  'SECRET_TOKEN': 'bOD4kLSAaIwETXMkGh',

  'SERVER_URL': 'https://8302e8dab20845b0a79774cc122a4364.apm.us-east-2.aws.elastic-cloud.com:443',

  'ENVIRONMENT': 'my-environment',
}
apm = ElasticAPM(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086) 