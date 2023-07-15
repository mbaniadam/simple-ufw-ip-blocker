GRANT ALL PRIVILEGES ON DATABASE wgpeers TO postgres;
\connect wgpeers
CREATE TABLE users (
        user_id serial PRIMARY KEY,
        username VARCHAR (255) NOT NULL,
        ip_address VARCHAR (255) NOT NULL UNIQUE,
        created_date DATE NOT NULL DEFAULT CURRENT_DATE,
		expire_date DATE NOT NULL,
        valid_days INT
);
