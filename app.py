from flask import Flask, render_template
from datetime import date, datetime, time, timedelta

app = Flask(__name__)
hoy = date.today()

# Sesiones
SESIONES = [
    ("Práctica 1", time(10,30)),
    ("Práctica 2", time(13,0)),
    ("Clasificación", time(15,0)),
    ("Sprint", time(11,30)),
    ("Carrera", time(14,30)),
]

# Datos
f2 = [
    {"fecha": date(2026,3,8),"zona":3,"lugar":"Melbourne","piloto":"Rafael Câmara","equipo":"Invicta"},
    {"fecha": date(2026,4,12),"zona":2,"lugar":"Bahrain","piloto":"Ritomo Miyata","equipo":"Hitech"},
]

f3 = [
    {"fecha": date(2026,3,8),"zona":3,"lugar":"Melbourne","piloto":"Ugo Ugochukwu","equipo":"Campos"},
    {"fecha": date(2026,7,5),"zona":1,"lugar":"Silverstone","piloto":"Mattia Colnaghi","equipo":"MP"},
]


# Hora Argentina
def hora_arg(fecha, hora, zona):
    dt = datetime.combine(fecha, hora)
    dt -= timedelta(hours=zona+3)
    return dt.strftime("%H:%M")


@app.route("/")
def home():

    f2_ordenado = sorted(f2, key=lambda x: x["fecha"])
    f3_ordenado = sorted(f3, key=lambda x: x["fecha"])

    return render_template(
        "index.html",
        f2=f2_ordenado,
        f3=f3_ordenado,
        sesiones=SESIONES,
        hora_arg=hora_arg,
        hoy=hoy
    )


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





