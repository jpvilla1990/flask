from flask import Flask, render_template, request
from tools.routeFunctions import RouteFunctions

app = Flask(__name__)
routeFunctions = RouteFunctions()

@app.route("/", methods=['GET', 'POST'])
def home():
    buttons = [
            "DMC-NaturaXL",
            "Drops-Safran",
            "Drops-BabyMerinoMix",
            "Stylecraft-SpecialDoubleKnit",
            #"Hahn-AlpaccaSpeciale",
            ]
    urls = [
            "https://www.wollplatz.de/wolle/dmc/dmc-natura-xl",
            "https://www.wollplatz.de/wolle/drops/drops-safran",
            "https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix",
            "https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk",
            ]
    templateRender = "home.html"
    OriginalRender = render_template(templateRender,
                             button1=buttons[0],
                             button2=buttons[1],
                             button3=buttons[2],
                             button4=buttons[3],
                             )
    buttonRender = routeFunctions.ButtonRequestHome(
            requestObject=request,
            buttons=buttons,
            render=templateRender,
            urls=urls,
            )
    if buttonRender != None:
        return buttonRender
    else:
        return OriginalRender
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8050)