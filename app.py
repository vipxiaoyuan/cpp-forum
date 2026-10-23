from flask import Flask,render_template,request,redirect,url_for
import time

app = Flask(__name__)

# 内存数据库，重启程序数据清空
posts = []
pid = 1

@app.route('/')
def index():
    return render_template("index.html",posts=posts)

@app.route('/post',methods=["GET","POST"])
def add_post():
    if request.method == "POST":
        global pid
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        posts.append({
            "id":pid,
            "author":author,
            "title":title,
            "content":content,
            "time":t
        })
        pid +=1
        return redirect("/")
    return render_template("post.html")

@app.route('/detail')
def detail():
    idx = int(request.args.get("id"))
    for p in posts:
        if p["id"] == idx:
            return render_template("detail.html",post=p)
    return "帖子不存在",404

if __name__ == '__main__':
    app.run(debug=True)
