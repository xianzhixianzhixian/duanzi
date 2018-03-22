create table daunzi
(
id bigint PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT 'id',
author varchar(50) NOT NULL DEFAULT '' COMMENT 'author',
context TEXT NOT NULL COMMENT 'detail of the article',
startnums int NOT NULL DEFAULT 0 COMMENT 'start numbers',
commentnums int NOT NULL DEFAULT 0 COMMENT 'comment numbers'
);