# from flask import Flask,render_template,url_for,redirect,flash,request,jsonify,json
# from flask import request
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import request
# from Crypto.Cipher import AES
# import os
# import base64

# dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(50), unique = True , nullable=False)
#     password = db.Column(db.String(80), nullable = False)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/search")
# def search():
#     pass

# @app.route("/signup", methods = ["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         hashed_pw = generate_password_hash(request.form["password"], method="sha256")
#         new_user = Users(username=request.form["username"], password=hashed_pw)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect(url_for("login"))

#     return render_template("signup.html")

# # @app.route("/login")
# # def login():
# #     if request.method == "POST":
# #         user = Users.query.filter_by(username=request.form["username"]).first()

# #         if user and check_password_hash(user.password,request.form["password"]):
# #             return "kcmsal"

# #     return render_template("login.html")
# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/demo", methods=["GET", "POST"])
# def demo():
#     if request.method == "POST":
#         nick_name = request.form.get("nick_name")
#         print(nick_name)
#         return "ok"
#     return render_template("login.html")   
    

# # @app.route('/process', methods=["GET", "POST"])
# # def process():
 
# #     if request.method == "POST":
# #         user = Users.query.filter_by(username=request.form["username"]).first()

# #         if user and check_password_hash(user.password,request.form["password"]):
# #             return "siaofnsiafnoasinfao"
# #     return request.form
# #     # return render_template("index.html")
    

 
# #     # return jsonify({'error' : 'Missing data!'})     
# my_key = "59424d1c2f4451c568cd173984fc8d46fa3ceabc27b255e714e34f59f12b355a"
# @app.route('/process', methods=["GET", "POST"])
# def process():
    

#     base64_message1=request.form["username"]
#     base64_bytes1 = base64_message1.encode('ascii')
#     message_bytes1 = base64.b64decode(base64_bytes1)
#     message1 = message_bytes1.decode('ascii')

#     base64_message2=request.form["password"]
#     base64_bytes2 = base64_message2.encode('ascii')
#     message_bytes2 = base64.b64decode(base64_bytes2)
#     message2 = message_bytes2.decode('ascii')

#     base64_message3=request.form["key"]
#     base64_bytes3 = base64_message3.encode('ascii')
#     message_bytes3 = base64.b64decode(base64_bytes3)
#     message3 = message_bytes3.decode('ascii')

#     print(message1)
#     print(message2)


#     if request.method == "POST" and message3 == my_key:
#         user = Users.query.filter_by(username=message1).first()

#         if user and check_password_hash(user.password,message2):
#             return "Ingreso correcto"
#         else:
#             return "Usuario o contraseña incorrectos"
#         print(check_password_hash(user.password,message2))


#     return render_template("login.html")
    

 
#     # return jsonify({'error' : 'Missing data!'}) 

# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)


import base64, codecs
magic = 'ZnJvbSBmbGFzayBpbXBvcnQgRmxhc2sscmVuZGVyX3RlbXBsYXRlLHVybF9mb3IscmVkaXJlY3QsZmxhc2gscmVxdWVzdCxqc29uaWZ5LGpzb24KZnJvbSBmbGFzayBpbXBvcnQgcmVxdWVzdApmcm9tIGZsYXNrX3NxbGFsY2hlbXkgaW1wb3J0IFNRTEFsY2hlbXkKZnJvbSB3ZXJremV1Zy5zZWN1cml0eSBpbXBvcnQgZ2VuZXJhdGVfcGFzc3dvcmRfaGFzaCwgY2hlY2tfcGFzc3dvcmRfaGFzaApmcm9tIGZsYXNrIGltcG9ydCByZXF1ZXN0CmZyb20gQ3J5cHRvLkNpcGhlciBpbXBvcnQgQUVTCmltcG9ydCBvcwppbXBvcnQgYmFzZTY0CgpkYmRpciA9ICJzcWxpdGU6Ly8vIiArIG9zLnBhdGguYWJzcGF0aChvcy5nZXRjd2QoKSkgKyAiL2RhdGFiYXNlLmRiIgoKYXBwID0gRmxhc2soX19uYW1lX18pCmFwcC5jb25maWdbIlNRTEFMQ0hFTVlfREFUQUJBU0VfVVJJIl0gPSBkYmRpcgphcHAuY29uZmlnWyJTUUxBTENIRU1ZX1RSQUNLX01PRElGSUNBVElPTlMiXSA9IEZhbHNlCmRiID0gU1FMQWxjaGVteShhcHApCgoKY2xhc3MgVXNlcnMoZGIuTW9kZWwpOgogICAgaWQgPSBkYi5Db2x1bW4oZGIuSW50ZWdlciwgcHJpbWFyeV9rZXkgPSBUcnVlKQogICAgdXNlcm5hbWUgPSBkYi5Db2x1bW4oZGIuU3RyaW5nKDUwKSwgdW5pcXVlID0gVHJ1ZSAsIG51bGxhYmxlPUZhbHNlKQogICAgcGFzc3dvcmQgPSBkYi5Db2x1bW4oZGIuU3RyaW5nKDgwKSwgbnVsbGFibGUgPSBGYWxzZSkKCkBhcHAucm91dGUoIi8iKQpkZWYgaW5kZXgoKToKICAgIHJldHVybiByZW5kZXJfdGVtcGxhdGUoImluZGV4Lmh0bWwiKQoKQGFwcC5yb3V0ZSgiL3NlYXJjaCIpCmRlZiBzZWFyY2goKToKICAgIHBhc3MKCkBhcHAucm91dGUoIi9zaWdudXAiLCBtZXRob2RzID0gWyJHRVQiLCAiUE9TVCJdKQpkZWYgc2lnbnVwKCk6CiAg'
love = 'VPOcMvOlMKS1MKA0Yz1yqTuiMPN9CFNvHR9GIPV6PvNtVPNtVPNtnTSmnTIxK3O3VQ0tM2IhMKWuqTIspTSmp3qipzEsnTSmnPulMKS1MKA0YzMipz1oVaOup3A3o3WxVy0fVT1yqTuiMQ0vp2uuZwH2VvxXVPNtVPNtVPOhMKqsqKAypvN9VSImMKWmXUImMKWhLJ1yCKWypKIyp3DhMz9loIfvqKAypz5uoJHvKFjtpTSmp3qipzD9nTSmnTIxK3O3XDbtVPNtVPNtVTEvYaAyp3Aco24hLJExXT5yq191p2IlXDbtVPNtVPNtVTEvYaAyp3Aco24hL29goJy0XPxXPvNtVPNtVPNtpzI0qKWhVUWyMTylMJA0XUIloS9zo3VbVzkiM2yhVvxcPtbtVPNtpzI0qKWhVUWyozEypy90MJ1joTS0MFtvp2yaoaIjYzu0oJjvXDbXVlONLKOjYaWiqKEyXPVioT9anJ4vXDbwVTEyMvOfo2qcovtcBtbwVPNtVPOcMvOlMKS1MKA0Yz1yqTuiMPN9CFNvHR9GIPV6PvZtVPNtVPNtVPO1p2IlVQ0tIKAypaZhpKIypaxhMzyfqTIlK2W5XUImMKWhLJ1yCKWypKIyp3DhMz9loIfvqKAypz5uoJHvKFxhMzylp3DbXDbXVlNtVPNtVPNtVTyzVUImMKVtLJ5xVTAbMJAeK3Oup3A3o3WxK2uup2tbqKAypv5jLKAmq29lMPklMKS1MKA0YzMipz1oVaOup3A3o3WxVy0cBtbwVPNtVPNtVPNtVPNtVUWyqUIlovNvn2Agp2SfVtbXVlNtVPNtpzI0qKWhVUWyozEypy90MJ1joTS0MFtvoT9anJ4hnUEgoPVcPxOupUNhpz91qTHbVv9fo2qcovVcPzEyMvOfo2qcovtcBtbtVPNtpzI0qKWhVUWyozEypy90MJ1joTS0MFtvoT9anJ4hnUEgoPVcPtcNLKOjYaWiqKEyXPViMTIgolVfVT1yqTuiMUZ9JlWUEIDvYPNvHR9GIPWqXDcxMJLtMTIgoltcBtbtVPNtnJLtpzIkqJImqP5gMKEbo2DtCG0tVyOCH1DvBtbtVPNtVPNtVT5cL2gsozSgMFN9VUWypKIyp3DhMz9loF5aMKDbVz5cL2gsozSgMFVcPvNtVPNtVPNtpUWcoaDbozywn19hLJ1yXDbtVPNtVPNt'
god = 'IHJldHVybiAib2siCiAgICByZXR1cm4gcmVuZGVyX3RlbXBsYXRlKCJsb2dpbi5odG1sIikgICAKICAgIAoKIyBAYXBwLnJvdXRlKCcvcHJvY2VzcycsIG1ldGhvZHM9WyJHRVQiLCAiUE9TVCJdKQojIGRlZiBwcm9jZXNzKCk6CiAKIyAgICAgaWYgcmVxdWVzdC5tZXRob2QgPT0gIlBPU1QiOgojICAgICAgICAgdXNlciA9IFVzZXJzLnF1ZXJ5LmZpbHRlcl9ieSh1c2VybmFtZT1yZXF1ZXN0LmZvcm1bInVzZXJuYW1lIl0pLmZpcnN0KCkKCiMgICAgICAgICBpZiB1c2VyIGFuZCBjaGVja19wYXNzd29yZF9oYXNoKHVzZXIucGFzc3dvcmQscmVxdWVzdC5mb3JtWyJwYXNzd29yZCJdKToKIyAgICAgICAgICAgICByZXR1cm4gInNpYW9mbnNpYWZub2FzaW5mYW8iCiMgICAgIHJldHVybiByZXF1ZXN0LmZvcm0KIyAgICAgIyByZXR1cm4gcmVuZGVyX3RlbXBsYXRlKCJpbmRleC5odG1sIikKICAgIAoKIAojICAgICAjIHJldHVybiBqc29uaWZ5KHsnZXJyb3InIDogJ01pc3NpbmcgZGF0YSEnfSkgICAgIApteV9rZXkgPSAiNTk0MjRkMWMyZjQ0NTFjNTY4Y2QxNzM5ODRmYzhkNDZmYTNjZWFiYzI3YjI1NWU3MTRlMzRmNTlmMTJiMzU1YSIKQGFwcC5yb3V0ZSgnL3Byb2Nlc3MnLCBtZXRob2RzPVsiR0VUIiwgIlBPU1QiXSkKZGVmIHByb2Nlc3MoKToKICAgIAoKICAgIGJhc2U2NF9tZXNzYWdlMT1yZXF1ZXN0LmZvcm1bInVzZXJuYW1lIl0KICAgIGJhc2U2NF9ieXRlczEgPSBiYXNlNjRfbWVzc2FnZTEuZW5jb2RlKCdhc2NpaScpCiAgICBtZXNzYWdlX2J5dGVzMSA9IGJhc2U2NC5iNjRkZWNvZGUoYmFzZTY0X2J5dGVzMSkKICAgIG1lc3NhZ2UxID0gbWVzc2FnZV9ieXRlczEuZGVjb2RlKCdhc2NpaScpCgogICAgYmFzZTY0X21lc3NhZ2UyPXJlcXVlc3QuZm9ybVsicGFzc3dvcmQiXQogICAgYmFz'
destiny = 'MGL0K2W5qTImZvN9VTWup2H2AS9gMKAmLJqyZv5yozAiMTHbW2SmL2ycWlxXVPNtVT1yp3AuM2IsLay0MKZlVQ0tLzSmMGL0YzV2ATEyL29xMFuvLKAyAwEsLay0MKZlXDbtVPNtoJImp2SaMGVtCFOgMKAmLJqyK2W5qTImZv5xMJAiMTHbW2SmL2ycWlxXPvNtVPOvLKAyAwEsoJImp2SaMGZ9pzIkqJImqP5zo3WgJlWeMKxvKDbtVPNtLzSmMGL0K2W5qTImZlN9VTWup2H2AS9gMKAmLJqyZl5yozAiMTHbW2SmL2ycWlxXVPNtVT1yp3AuM2IsLay0MKZmVQ0tLzSmMGL0YzV2ATEyL29xMFuvLKAyAwEsLay0MKZmXDbtVPNtoJImp2SaMGZtCFOgMKAmLJqyK2W5qTImZl5xMJAiMTHbW2SmL2ycWlxXPvNtVPOjpzyhqPugMKAmLJqyZFxXVPNtVUOlnJ50XT1yp3AuM2HlXDbXPvNtVPOcMvOlMKS1MKA0Yz1yqTuiMPN9CFNvHR9GIPVtLJ5xVT1yp3AuM2HmVQ09VT15K2gyrGbXVPNtVPNtVPO1p2IlVQ0tIKAypaZhpKIypaxhMzyfqTIlK2W5XUImMKWhLJ1yCJ1yp3AuM2HkXF5znKWmqPtcPtbtVPNtVPNtVTyzVUImMKVtLJ5xVTAbMJAeK3Oup3A3o3WxK2uup2tbqKAypv5jLKAmq29lMPkgMKAmLJqyZvx6PvNtVPNtVPNtVPNtVUWyqUIlovNvFJ5apzImolOwo3WlMJA0olVXVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPOlMKE1pz4tVyImqJSlnJ8tolOwo250pzSmMpBkLFOcozAipaWyL3EiplVXVPNtVPNtVPOjpzyhqPuwnTIwn19jLKAmq29lMS9bLKAbXUImMKVhpTSmp3qipzDfoJImp2SaMGVcXDbXPvNtVPOlMKE1pz4tpzIhMTIlK3EyoKOfLKEyXPWfo2qcov5bqT1fVvxXVPNtVNbXVNbtVPNtVlOlMKE1pz4tnaAiozyzrFu7W2Ilpz9lWlN6VPqAnKAmnJ5aVTEuqTRuW30cVNbXnJLtK19hLJ1yK18tCG0tVy9soJScoy9sVwbXVPNtVTEvYzAlMJS0MI9uoTjbXDbtVPNtLKOjYaW1ovuxMJW1Mm1HpaIyXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))