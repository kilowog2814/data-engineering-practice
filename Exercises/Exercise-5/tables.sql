DROP TABLE IF EXISTS tb_accounts;
DROP TABLE IF EXISTS tb_products;
DROP TABLE IF EXISTS tb_transactions;


CREATE TABLE tb_accounts (
    customer_id int PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(100),
    address_1 varchar(100),
    address_2 varchar(100),
    city varchar(20),
    state varchar(30),
    zip_code int,
    join_date date
);

CREATE TABLE tb_products (
    product_id int PRIMARY KEY,
    product_code int,
    product_description varchar(100)
);

CREATE TABLE tb_transactions (
    transaction_id varchar(30) PRIMARY KEY,
    transaction_date date,
    product_id int,
    product_code int ,
    product_description varchar(100),
    quantity int, 
    account_id int
);