CREATE TABLE logs (
	id SERIAL,
  	field_created_at DATETIME NOT NULL,
	table_name VARCHAR(20) NOT NULL,
	field_id BIGINT UNSIGNED NOT NULL,
	field_name VARCHAR(255)
	) ENGINE=ARCHIVE;