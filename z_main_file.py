from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        num_players = request.form.get('players')
        print(num_players)
        return redirect(f'players/{num_players}')
    return render_template ("number_players.html")

@app.route('/players/<num_players>', methods=['GET', 'POST'])
# def players(num_players):
#     if request.method == "POST":
#         name1 = request.form.get('login1')
#         name2 = request.form.get('login2')
#         name3 = request.form.get('login3')
#         name4 = request.form.get('login4')
#         print(name1)
#         print(name2)
#         print(name3)
#         print(name4)
def players(num_players):
    name1 = name2 = name3 = name4 = ""
    if request.method == "POST":
        if num_players == "1":
            gravetc1 = request.form.get('gravetc1')
            print(gravetc1)
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            print(name1)
            print(name2)
            print(name3)
            print(name4)
        if num_players == "2":
            gravetc1 = request.form.get('gravetc1')
            print(gravetc1)
            gravetc2 = request.form.get('gravetc2')
            print(gravetc2)
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            print(name1)
            print(name2)
            print(name3)
            print(name4)
        if num_players == "3":
            gravetc1 = request.form.get('gravetc1')
            print(gravetc1)
            gravetc2 = request.form.get('gravetc2')
            print(gravetc2)
            gravetc3 = request.form.get('gravetc3')
            print(gravetc3)
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            print(name1)
            print(name2)
            print(name3)
            print(name4)
        if num_players == "4":
            gravetc1 = request.form.get('gravetc1')
            print(gravetc1)
            gravetc2 = request.form.get('gravetc2')
            print(gravetc2)
            gravetc3 = request.form.get('gravetc3')
            print(gravetc3)
            gravetc4 = request.form.get('gravetc4')
            print(gravetc4)
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            print(name1)
            print(name2)
            print(name3)
            print(name4)
        # return redirect(url_for('menu', num_players=num_players))
        return render_template("menu.html", name1=name1, name2=name2, name3=name3, name4=name4)
    return render_template('player_names.html', num_players = num_players)





# @app.route("/menu", methods=['GET', 'POST'])
# def menu():
#     if request.method == "POST":
#         # print(request.form["stiyka"])
#         # print(request.form["legka"])
#         if "legka" in request.form:
#             return redirect(url_for("str_leg"))
#             print(1)
#         elif "stiyka" in request.form:
#             return redirect(url_for("str_st"))
#             print(2)
#         elif "hod" in request.form:
#             return redirect(url_for("hid"))
#             print(3)
#     return render_template("menu.html")
    



@app.route("/hid")
def hid():
    return render_template("hid.html")

@app.route("/str_st")
def str_st():
    return render_template("str_st.html")

@app.route("/str_leg")
def str_leg():
    return render_template("str_leg.html")


@app.route("/res_str_leg/<int:button_number>")
def res_str_leg(button_number):
    return render_template("str_leg_res.html", button_number=button_number)


app.config["SECRET_KEY"] = "MySecretKey"
if __name__ == "__main__":
    app.run(debug=True)