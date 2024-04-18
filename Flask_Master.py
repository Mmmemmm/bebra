from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/contacts/")
def contacts():
    #Где то взяли данные
    developer_name = 'Ilon Mask'
    devoloper_phone = '88005553555555555555'
    developer_adress= ('улица Карла Маркса 52 Чебоксары Чувашская - '
                       'Чувашия Републиц, Чебоксары, Чувашская Респ., 428003')
    #Контекст - те данные, которые мы передаем из контроллера в шаблон
    return render_template('contacts.html', name = developer_name, phone=devoloper_phone,address = developer_adress)

@app.route("/information/")
def information():
    #Где то взяли данные
    site_info='Это первый тестовый сайт на Flask'
    return render_template('information.html', info = site_info)

@app.route("/donate/")
def donate():
    #Где то взяли данные
    donate='https://www.donationalerts.com/r/tabikriki'
    return render_template('donate.html', donate = donate)


if __name__ == "__main__":
    app.run(debug= True)