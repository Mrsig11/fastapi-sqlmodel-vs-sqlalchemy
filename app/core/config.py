import os



ORM_ENGINE = os.getenv("ORM_ENGINE", "sqlmodel")

print(ORM_ENGINE)
# ORM_ENGINE = os.getenv("ORM_ENGINE", "sqlalchemy")