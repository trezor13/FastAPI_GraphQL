from orator import DatabaseManager, Schema, Model

# I am using online DB hano kugirango nkore test ariko wowe you can configure DB yawe bisanzwe
DATABASES = "postgres://zbrzebxz:hXEVJpPMUMsckc0uRIEAjcNHsq0Cf4lm@kesavan.db.elephantsql.com/abrzebxz"

# Database iri local
# DATABASES = {
#     "postgres": {
#         "driver": "postgres",
#         "host": "localhost",
#         "database": "postgres",
#         "user": "postgres",
#         "password": "postgres",
#         "prefix": "",
#         "port": 5433
#     }
# }

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
