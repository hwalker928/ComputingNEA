CREATE TABLE `credentials` (
	`id` INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	`last_used_at` DATETIME,
	`name` TEXT(65535) NOT NULL,
	`username` TEXT(65535),
	`password` TEXT(65535),
	`domain` TEXT(65535),
	`two_factor_id` INTEGER,
	`created_at` DATETIME NOT NULL,
	`updated_at` DATETIME NOT NULL,
	`tag_id` INTEGER,
	PRIMARY KEY(`id`)
);

CREATE TABLE `user_details` (
	`id` INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	`key` TEXT(65535) NOT NULL,
	`value` TEXT(65535) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `generated_passwords` (
	`id` INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	`password` TEXT(65535) NOT NULL,
	`generated_at` DATETIME NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `tags` (
	`id` INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	`name` TEXT(64) NOT NULL,
	`colour` TEXT(6),
	PRIMARY KEY(`id`)
);


CREATE TABLE `two_factor` (
	`id` INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	`token` TEXT(65535) NOT NULL,
	PRIMARY KEY(`id`)
);