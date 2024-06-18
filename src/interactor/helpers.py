import database.config as db_config


def parse_db_type_and_version(arg: str) -> db_config.DatabaseTypeAndVersion:
    """
    Parses the database version and type from the given string.
    """

    is_local = False
    if arg.endswith("local"):
        arg = arg[:-6]
        is_local = True

    parts = arg.replace("-", " ").split()
    if len(parts) != 2:
        raise ValueError(
            "Invalid format. Use <DB TYPE>-<VERSION> or <DB TYPE>-<VERSION>-local."
        )

    db_type = db_config.DatabaseType.from_str(parts[0])
    version = parts[1]
    return db_config.DatabaseTypeAndVersion(db_type, version, not is_local)
