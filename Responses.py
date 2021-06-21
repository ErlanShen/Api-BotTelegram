from datetime import datetime

def sample_respondes(input_text):
    user_message = str(input_text).lower()

    if user_message in ("HOLA", 'hi', 'hola'):
        return "Bienvenido a mi bot: Preguntame la hora"

    if user_message in ("Hora?", "time", "la hora", "que hora es"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "No entiendo la orden, Intenta una vez mas!"