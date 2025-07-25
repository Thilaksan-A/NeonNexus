# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# cors = CORS(app, origins='*')


# @app.route("/api/users", methods=['GET'])
# def users():
#     return jsonify(
#         {
#             "users":[
#                 'arpan',
#                 'zach',
#                 'jessie'
#             ]
#         }
#     )

from app import create_app

app = create_app()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()