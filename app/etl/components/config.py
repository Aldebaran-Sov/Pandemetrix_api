mariadb_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'password',
    'database': 'api'
}

postgres_raw_config = {
    'host': 'postgresql_raw',
    'database': 'raw_db',
    'username': 'raw_user',
    'password': 'raw_password',
    'port': '5432'
}

# TODO: Automatiser les config en créant des variables d'env dans le docker-compose