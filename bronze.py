import duckdb

con = duckdb.connect('DataWarehouse.duckdb')

def load_bronze():

    _ = con.execute("""
        CREATE SCHEMA IF NOT EXISTS bronze;
        CREATE SCHEMA IF NOT EXISTS silver;
        CREATE SCHEMA IF NOT EXISTS gold;
    """)

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

    _ = con.execute("""
        TRUNCATE TABLE bronze.crm_cust_info;
    """)

    _ = con.execute(
        """
        COPY bronze.crm_cust_info
        FROM '/home/pinaka/projects/DataWarehouse/source_crm/cust_info.csv'
        (HEADER, DELIMITER ',')
        """
    )

    _ = con.execute(
        """
        TRUNCATE TABLE bronze.crm_prd_info
        """
    )

    _ = con.sql(
        """
        COPY bronze.crm_prd_info
        FROM '/home/pinaka/projects/DataWarehouse/source_crm/prd_info.csv'
        (HEADER, DELIMITER ',')
        """
    )

    _ = con.execute(
        """
        TRUNCATE TABLE bronze.crm_sales_details
        """
    )

    _ = con.sql(
        """
        COPY bronze.crm_sales_details
        FROM '/home/pinaka/projects/DataWarehouse/source_crm/sales_details.csv'
        (HEADER, DELIMITER ',')
        """
    )

    _ = con.execute(
        """
        TRUNCATE TABLE bronze.erp_cust_az12
        """
    )

    _ = con.sql(
        """
        COPY bronze.erp_cust_az12
        FROM '/home/pinaka/projects/DataWarehouse/source_erp/CUST_AZ12.csv'
        (HEADER, DELIMITER ',')
        """
    )

    _ = con.execute(
        """
        TRUNCATE TABLE bronze.erp_loc_a101
        """
    )

    _ = con.sql(
        """
        COPY bronze.erp_loc_a101
        FROM '/home/pinaka/projects/DataWarehouse/source_erp/LOC_A101.csv'
        (HEADER, DELIMITER ',')
        """
    )

    _ = con.execute(
        """
        TRUNCATE TABLE bronze.erp_px_cat_g1v2
        """
    )

    _ = con.sql(
        """
        COPY bronze.erp_px_cat_g1v2
        FROM '/home/pinaka/projects/DataWarehouse/source_erp/PX_CAT_G1V2.csv'
        (HEADER, DELIMITER ',')
        """
    )

    df1 = con.sql(
        """
        select count(*) from bronze.crm_cust_info
        """
    )

    print(df1)

if __name__ == "__main__":
    load_bronze()
