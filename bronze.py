import duckdb

con = duckdb.connect(':memory:')

_ = con.execute(
    """
    create schema Bronze;
    create schema Silver;
    create schema Gold;
    """
)
