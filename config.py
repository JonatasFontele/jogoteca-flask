# Configs for the project

# Encryption layer secret key on the website “app.secret_key"
SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='',
        servidor='',
        porta='',
        database=''
    )
