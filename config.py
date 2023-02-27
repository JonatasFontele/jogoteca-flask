# Configs for the project

# Encryption layer secret key on the website “app.secret_key"
SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='x9hjB5JJ0pRird61NJhp',
        servidor='containers-us-west-163.railway.app',
        porta='7063',
        database='railway'
    )
