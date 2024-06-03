import database.config as db_config


def parse_db_type_and_version(arg) -> db_config.DatabaseTypeAndVersion:
    """
    Parses the database version and type from the given string.
    """
    parts = arg.replace("-", " ").split()
    if len(parts) != 2:
        raise ValueError("Invalid format. Use <DB TYPE>-<VERSION>.")
    db_type = db_config.DatabaseType.from_str(parts[0])
    version = parts[1]
    return db_config.DatabaseTypeAndVersion(db_type, version)
