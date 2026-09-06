import duckdb

con = duckdb.connect(':memory:')

_ = con.execute(
    """
    create schema Bronze;
    create schema Silver;
    create schema Gold;
    """
)

_ = con.execute(
    """
    create table bronze.crm_cust_info(
        cst_id INT,
        cst_key NVARCHAR(50),
        cst_firstname NVARCHAR(50),
        cst_lastname NVARCHAR(50),
        cst_material_status NVARCHAR(50),
        cst_gndr NVARCHAR(50),
        cst_create_date DATE
    )
    """
)

_ = con.execute(
    """
    create table bronze.crm_prd_info(
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
    create table bronze.crm_sales_details(
        sls_ord_num INT,
        sls_prd_key NVARCHAR(50),
        sls_cust_id NVARCHAR(50),
        sls_order_dt DATE,
        sls_ship_dt DATE,
        sls_due_dt DATE,
        sls_sales INT,
        sls_quantity INT,
        sls_price INT
    )
    """
)

_ = con.execute(
    """
    create table bronze.erp_cust_az12 (
        CID NVARCHAR(50),
        BDATE DATE,
        GEN NVARCHAR(50)
    )
    """
)

_ = con.execute(
    """
    create table bronze.erp_loc_a101 (
        CID NVARCHAR(50),
        CNTRY NVARCHAR(50)
    )
    """
)

_ = con.execute(
    """
    create table bronze.erp_px_cat_g1v2 (
        ID NVARCHAR(50),
        CAT NVARCHAR(50),
        SUBCAT NVARCHAR(50),
        MAINTENANCE NVARCHAR(50)
    )
    """
)
