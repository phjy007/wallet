BEGIN;
CREATE TABLE `wallet_wiki_user_fans` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `from_user_id` integer NOT NULL,
    `to_user_id` integer NOT NULL,
    UNIQUE (`from_user_id`, `to_user_id`)
)
;
CREATE TABLE `wallet_wiki_user_following` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `from_user_id` integer NOT NULL,
    `to_user_id` integer NOT NULL,
    UNIQUE (`from_user_id`, `to_user_id`)
)
;
CREATE TABLE `wallet_wiki_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `username` varchar(200) NOT NULL,
    `password` varchar(32) NOT NULL,
    `nickname` varchar(50) NOT NULL,
    `email` varchar(200) NOT NULL,
    `portrait` varchar(100) NOT NULL
)
;
ALTER TABLE `wallet_wiki_user_fans` ADD CONSTRAINT `from_user_id_refs_id_ab78abef` FOREIGN KEY (`from_user_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_user_fans` ADD CONSTRAINT `to_user_id_refs_id_ab78abef` FOREIGN KEY (`to_user_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_user_following` ADD CONSTRAINT `from_user_id_refs_id_fcbb3b2f` FOREIGN KEY (`from_user_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_user_following` ADD CONSTRAINT `to_user_id_refs_id_fcbb3b2f` FOREIGN KEY (`to_user_id`) REFERENCES `wallet_wiki_user` (`id`);
CREATE TABLE `wallet_wiki_super_admin` (
    `user_ptr_id` integer NOT NULL PRIMARY KEY
)
;
ALTER TABLE `wallet_wiki_super_admin` ADD CONSTRAINT `user_ptr_id_refs_id_ceab6a22` FOREIGN KEY (`user_ptr_id`) REFERENCES `wallet_wiki_user` (`id`);
CREATE TABLE `wallet_wiki_inbox` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `wallet_wiki_inbox` ADD CONSTRAINT `user_id_refs_id_29292b79` FOREIGN KEY (`user_id`) REFERENCES `wallet_wiki_user` (`id`);
CREATE TABLE `wallet_wiki_inbox_item` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `inbox_id` integer NOT NULL,
    `msg_type` integer NOT NULL,
    `brief_content` longtext NOT NULL,
    `time` datetime NOT NULL
)
;
ALTER TABLE `wallet_wiki_inbox_item` ADD CONSTRAINT `inbox_id_refs_id_4ecb9fc` FOREIGN KEY (`inbox_id`) REFERENCES `wallet_wiki_inbox` (`id`);
CREATE TABLE `wallet_wiki_category` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `category_name` varchar(100) NOT NULL
)
;
CREATE TABLE `wallet_wiki_keyword` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `keyword_name` varchar(20) NOT NULL,
    `author_id` integer NOT NULL
)
;
ALTER TABLE `wallet_wiki_keyword` ADD CONSTRAINT `author_id_refs_id_9e666dce` FOREIGN KEY (`author_id`) REFERENCES `wallet_wiki_user` (`id`);
CREATE TABLE `wallet_wiki_article_meta_category` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `article_meta_id` integer NOT NULL,
    `category_id` integer NOT NULL,
    UNIQUE (`article_meta_id`, `category_id`)
)
;
ALTER TABLE `wallet_wiki_article_meta_category` ADD CONSTRAINT `category_id_refs_id_2d94ed0f` FOREIGN KEY (`category_id`) REFERENCES `wallet_wiki_category` (`id`);
CREATE TABLE `wallet_wiki_article_meta_siting_article` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `from_article_meta_id` integer NOT NULL,
    `to_article_meta_id` integer NOT NULL,
    UNIQUE (`from_article_meta_id`, `to_article_meta_id`)
)
;
CREATE TABLE `wallet_wiki_article_meta_keyword` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `article_meta_id` integer NOT NULL,
    `keyword_id` integer NOT NULL,
    UNIQUE (`article_meta_id`, `keyword_id`)
)
;
ALTER TABLE `wallet_wiki_article_meta_keyword` ADD CONSTRAINT `keyword_id_refs_id_1789044b` FOREIGN KEY (`keyword_id`) REFERENCES `wallet_wiki_keyword` (`id`);
CREATE TABLE `wallet_wiki_article_meta_sited_article` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `from_article_meta_id` integer NOT NULL,
    `to_article_meta_id` integer NOT NULL,
    UNIQUE (`from_article_meta_id`, `to_article_meta_id`)
)
;
CREATE TABLE `wallet_wiki_article_meta` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(200) NOT NULL,
    `author_id` integer NOT NULL
)
;
ALTER TABLE `wallet_wiki_article_meta` ADD CONSTRAINT `author_id_refs_id_6294be48` FOREIGN KEY (`author_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_article_meta_category` ADD CONSTRAINT `article_meta_id_refs_id_254b3c61` FOREIGN KEY (`article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_article_meta_siting_article` ADD CONSTRAINT `from_article_meta_id_refs_id_2911be54` FOREIGN KEY (`from_article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_article_meta_siting_article` ADD CONSTRAINT `to_article_meta_id_refs_id_2911be54` FOREIGN KEY (`to_article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_article_meta_keyword` ADD CONSTRAINT `article_meta_id_refs_id_272e718d` FOREIGN KEY (`article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_article_meta_sited_article` ADD CONSTRAINT `from_article_meta_id_refs_id_dba2785a` FOREIGN KEY (`from_article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_article_meta_sited_article` ADD CONSTRAINT `to_article_meta_id_refs_id_dba2785a` FOREIGN KEY (`to_article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
CREATE TABLE `wallet_wiki_article` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `meta_id` integer NOT NULL,
    `version` integer UNSIGNED NOT NULL,
    `content` longtext NOT NULL,
    `time` datetime NOT NULL
)
;
ALTER TABLE `wallet_wiki_article` ADD CONSTRAINT `meta_id_refs_id_e9124b9c` FOREIGN KEY (`meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
CREATE TABLE `wallet_wiki_draft` (
    `article_ptr_id` integer NOT NULL PRIMARY KEY
)
;
ALTER TABLE `wallet_wiki_draft` ADD CONSTRAINT `article_ptr_id_refs_id_792649f2` FOREIGN KEY (`article_ptr_id`) REFERENCES `wallet_wiki_article` (`id`);
CREATE TABLE `wallet_wiki_collection_keyword` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `collection_id` integer NOT NULL,
    `keyword_id` integer NOT NULL,
    UNIQUE (`collection_id`, `keyword_id`)
)
;
ALTER TABLE `wallet_wiki_collection_keyword` ADD CONSTRAINT `keyword_id_refs_id_cc8bb075` FOREIGN KEY (`keyword_id`) REFERENCES `wallet_wiki_keyword` (`id`);
CREATE TABLE `wallet_wiki_collection` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `article_meta_id` integer NOT NULL,
    `article_version` integer UNSIGNED NOT NULL,
    `collect_time` datetime NOT NULL,
    `belong_to_id` integer NOT NULL
)
;
ALTER TABLE `wallet_wiki_collection` ADD CONSTRAINT `article_meta_id_refs_id_c6141b3f` FOREIGN KEY (`article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
ALTER TABLE `wallet_wiki_collection` ADD CONSTRAINT `belong_to_id_refs_id_eda5fdac` FOREIGN KEY (`belong_to_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_collection_keyword` ADD CONSTRAINT `collection_id_refs_id_5ec426f9` FOREIGN KEY (`collection_id`) REFERENCES `wallet_wiki_collection` (`id`);
CREATE TABLE `wallet_wiki_comment` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `time` datetime NOT NULL,
    `content` longtext NOT NULL,
    `author_id` integer NOT NULL,
    `article_meta_id` integer NOT NULL
)
;
ALTER TABLE `wallet_wiki_comment` ADD CONSTRAINT `author_id_refs_id_b5ee5e1c` FOREIGN KEY (`author_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_comment` ADD CONSTRAINT `article_meta_id_refs_id_e7af1289` FOREIGN KEY (`article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
CREATE TABLE `wallet_wiki_attachment` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `attachment_type` varchar(100) NOT NULL,
    `attachment_file` varchar(100) NOT NULL,
    `pathname` varchar(255) NOT NULL,
    `article_meta_id` integer NOT NULL
)
;
ALTER TABLE `wallet_wiki_attachment` ADD CONSTRAINT `article_meta_id_refs_id_b34e7bae` FOREIGN KEY (`article_meta_id`) REFERENCES `wallet_wiki_article_meta` (`id`);
CREATE TABLE `wallet_wiki_message` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `from_user_id` integer NOT NULL,
    `to_user_id` integer NOT NULL,
    `content` longtext NOT NULL,
    `time` datetime NOT NULL,
    `has_read` bool NOT NULL
)
;
ALTER TABLE `wallet_wiki_message` ADD CONSTRAINT `from_user_id_refs_id_6608b7aa` FOREIGN KEY (`from_user_id`) REFERENCES `wallet_wiki_user` (`id`);
ALTER TABLE `wallet_wiki_message` ADD CONSTRAINT `to_user_id_refs_id_6608b7aa` FOREIGN KEY (`to_user_id`) REFERENCES `wallet_wiki_user` (`id`);
CREATE INDEX `wallet_wiki_inbox_item_e569965d` ON `wallet_wiki_inbox_item` (`inbox_id`);
CREATE INDEX `wallet_wiki_keyword_cc846901` ON `wallet_wiki_keyword` (`author_id`);
CREATE INDEX `wallet_wiki_article_meta_cc846901` ON `wallet_wiki_article_meta` (`author_id`);
CREATE INDEX `wallet_wiki_article_9805f4bb` ON `wallet_wiki_article` (`meta_id`);
CREATE INDEX `wallet_wiki_collection_da6361b6` ON `wallet_wiki_collection` (`article_meta_id`);
CREATE INDEX `wallet_wiki_collection_f6751186` ON `wallet_wiki_collection` (`belong_to_id`);
CREATE INDEX `wallet_wiki_comment_cc846901` ON `wallet_wiki_comment` (`author_id`);
CREATE INDEX `wallet_wiki_comment_da6361b6` ON `wallet_wiki_comment` (`article_meta_id`);
CREATE INDEX `wallet_wiki_attachment_da6361b6` ON `wallet_wiki_attachment` (`article_meta_id`);
CREATE INDEX `wallet_wiki_message_8b4ff41f` ON `wallet_wiki_message` (`from_user_id`);
CREATE INDEX `wallet_wiki_message_ceab885c` ON `wallet_wiki_message` (`to_user_id`);
COMMIT;
