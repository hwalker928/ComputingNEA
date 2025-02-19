CREATE TABLE `credentials` (
	`id` INTEGER PRIMARY KEY,
	`name` TEXT(65535) NOT NULL,
	`username` TEXT(65535),
	`password` TEXT(65535),
	`domain` TEXT(65535),
	`two_factor_id` TEXT(65535),
	`created_at` DATETIME NOT NULL,
	`updated_at` DATETIME NOT NULL,
	`last_used_at` DATETIME,
	`tag_id` INTEGER
);

CREATE TABLE `user_details` (
	`id` INTEGER PRIMARY KEY,
	`key` TEXT(65535) NOT NULL,
	`value` TEXT(65535) NOT NULL
);


CREATE TABLE `generated_passwords` (
	`id` INTEGER PRIMARY KEY,
	`password` TEXT(65535) NOT NULL,
	`generated_at` DATETIME NOT NULL
);


CREATE TABLE `tags` (
	`id` INTEGER PRIMARY KEY,
	`name` TEXT(64) NOT NULL,
	`colour` TEXT(6)
);


CREATE TABLE `two_factor` (
	`id` INTEGER PRIMARY KEY,
	`token` TEXT(65535) NOT NULL
);