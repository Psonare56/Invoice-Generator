-- Grant all privileges on the database to the specified user
GRANT ALL PRIVILEGES ON DATABASE invoice_db TO invoice_user;

-- Grant all privileges on tables in the public schema to invoice_user
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO invoice_user;

-- Change ownership of the public schema to invoice_user
ALTER SCHEMA public OWNER TO invoice_user;

-- Set the validity of the invoice_user role to infinity
ALTER ROLE invoice_user VALID UNTIL 'infinity';

-- Grant superuser privileges to invoice_user
ALTER ROLE invoice_user SUPERUSER;

-- Grant permission to create roles to invoice_user
ALTER ROLE invoice_user CREATEROLE;

-- Grant permission to create databases to invoice_user
ALTER ROLE invoice_user CREATEDB;

-- Grant permission for replication to invoice_user (if needed)
ALTER ROLE invoice_user REPLICATION;

-- Grant permission to bypass RLS (Row Level Security) to invoice_user
ALTER ROLE invoice_user BYPASSRLS;
