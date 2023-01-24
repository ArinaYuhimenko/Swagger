#!/usr/bin/env python3
#http://localhost:8081/api/v1//ui/

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'OpenAPI домашняя видеотека'}, pythonic_params=True)
    app.run(port=8081)


if __name__ == '__main__':
    main()
