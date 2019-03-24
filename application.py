from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

matches = {}

@api.route('/<string:match_id>')
class LogMatches(Resource):
    def get(self, match_id):
        return {match_id: matches[match_id]}

    def put(self, match_id):
        matches[match_id] = request.form['result']
        return {match_id: matches[match_id]}

if __name__ == '__main__':
    app.run(debug=True)