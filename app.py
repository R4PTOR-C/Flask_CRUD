from config import DevelopmentConfig, ProductionConfig
from flask import Flask, render_template
import psycopg2


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)



@app.route('/')
def show_table():
    # Código para buscar dados da tabela no banco de dados
    # Substitua <sua_query> pela consulta SQL que recupera os dados da tabela
    conn = psycopg2.connect(host='localhost', user='rafael', password='nova_senha', database='banco_de_dados')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Renderizar o template HTML e passar os dados para a página
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
