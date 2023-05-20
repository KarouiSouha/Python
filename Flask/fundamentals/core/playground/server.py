from flask import Flask, render_template  # added render_template!
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template('index.html',times=3)
@app.route('/play/<int:num>')
def boxes(num):
    return render_template('index.html',times=num)
@app.route('/play/<int:num>/<color_change>') 
def change(num, color_change):
   return render_template('index.html', times=num, color=color_change)
if __name__=="__main__":
    app.run(debug=True) 

