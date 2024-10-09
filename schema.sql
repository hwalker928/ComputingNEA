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
