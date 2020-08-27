DROP TABLE IF EXISTS `new_monster`;
CREATE TABLE `new_monster` (
  `card_id` varchar(10) NOT NULL,
  `hash_code` varchar(10) NOT NULL,
  `package_no` varchar(64) DEFAULT NULL,
  `package_name` varchar(20) DEFAULT NULL, 
  `cn_name` varchar(64) DEFAULT NULL,
  `en_name` varchar(64) DEFAULT NULL,
  `jp_name` varchar(64) DEFAULT NULL,
  `nw_name` varchar(64) DEFAULT NULL,
  `card_no` varchar(64) DEFAULT NULL, 
  `rarity` varchar(64) DEFAULT NULL, 
  PRIMARY KEY (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

