import duckdb


def load_bronze():

    con = duckdb.connect('DataWarehouse.duckdb')

    try:
        print('Starting bronze layer load...')

        # --------------------------------------------------
        # 1. Create schemas
        # --------------------------------------------------

        _ = con.execute("""
            CREATE SCHEMA IF NOT EXISTS bronze;
            CREATE SCHEMA IF NOT EXISTS silver;
            CREATE SCHEMA IF NOT EXISTS gold;
        """)

        # --------------------------------------------------
        # 1. Create tables
        # --------------------------------------------------

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.crm_cust_info(
                cst_id INT,
                cst_key NVARCHAR(50),
                cst_firstname NVARCHAR(50),
                cst_lastname NVARCHAR(50),
                cst_marital_status NVARCHAR(50),
                cst_gndr NVARCHAR(50),
                cst_create_date DATE
            )
            """
        )

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.crm_prd_info(
                prd_id INT,
                prd_key NVARCHAR(50),
                prd_nm NVARCHAR(50),
                prd_cost INT,
                prd_line NVARCHAR(50),
                prd_start_dt DATE,
                prd_end_dt DATE
            )
            """
        )

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.crm_sales_details(
                sls_ord_num NVARCHAR(50),
                sls_prd_key NVARCHAR(50),
                sls_cust_id NVARCHAR(50),
                sls_order_dt VARCHAR(8),
                sls_ship_dt VARCHAR(8),
                sls_due_dt VARCHAR(8),
                sls_sales INT,
                sls_quantity INT,
                sls_price INT
            )
            """
        )

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.erp_cust_az12 (
                CID NVARCHAR(50),
                BDATE DATE,
                GEN NVARCHAR(50)
            )
            """
        )

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.erp_loc_a101 (
                CID NVARCHAR(50),
                CNTRY NVARCHAR(50)
            )
            """
        )

        _ = con.execute(
            """
            create table IF NOT EXISTS bronze.erp_px_cat_g1v2 (
                ID NVARCHAR(50),
                CAT NVARCHAR(50),
                SUBCAT NVARCHAR(50),
                MAINTENANCE NVARCHAR(50)
            )
            """
        )

        # --------------------------------------------------
        # 1. Load Tables
        # --------------------------------------------------

        tables = [
            (
                "crm_cust_info",
                "/home/pinaka/projects/DataWarehouse/source_crm/cust_info.csv"
            ),
            (
                "crm_prd_info",
                "/home/pinaka/projects/DataWarehouse/source_crm/prd_info.csv"
            ),
            (
                "crm_sales_details",
                "/home/pinaka/projects/DataWarehouse/source_crm/sales_details.csv"
            ),
            (
                "erp_cust_az12",
                "/home/pinaka/projects/DataWarehouse/source_erp/CUST_AZ12.csv"
            ),
            (
                "erp_loc_a101",
                "/home/pinaka/projects/DataWarehouse/source_erp/LOC_A101.csv"
            ),
            (
                "erp_px_cat_g1v2",
                "/home/pinaka/projects/DataWarehouse/source_erp/PX_CAT_G1V2.csv"
            )
        ]

        for table, file_path in tables:
            try:
                print(f"Loading {tables}...")

                _ = con.execute(
                    f"""
                    TRUNCATE TABLE bronze.{table}
                    """
                )

                _ = con.execute(
                    f"""
                    COPY bronze.{table}
                    FROM '{file_path}'
                    (HEADER, DELIMITER ',')
                    """
                )

                result = con.execute(
                    f"""
                    SELECT COUNT(*) FROM bronze.{table}
                    """
                ).fetchone()

                row_count = result[0] if result else 0

                print(f"✓ {table} loaded successfully: {row_count:,} rows")

            except Exception as e:
                print(f"✗ Failed to load {table}")
                print(f"  Error: {e}")

                raise

        print("Bronze layer load completed successfully.")

    except Exception as e:
        print('=================================================================')
        print('Bronze layer Failed')
        print(f"Error: {e}")
        print('=================================================================')

        raise

    finally:
        con.close()
if __name__ == "__main__":
    load_bronze()
