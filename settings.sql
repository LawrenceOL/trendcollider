-- settings.sql
CREATE DATABASE trend_collider;
CREATE USER tc_user WITH PASSWORD 'trend';
GRANT ALL PRIVILEGES ON DATABASE trend_collider TO tc_user;