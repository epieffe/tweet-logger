
CREATE TABLE `hashtag_tweet` (
  `tweet_id` bigint(20) NOT NULL,
  `hashtag_text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tweet` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `lang` varchar(255) NOT NULL,
  `in_reply_id` bigint(20) DEFAULT NULL,
  `retweet_id` bigint(20) DEFAULT NULL,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `hashtag_tweet`
  ADD PRIMARY KEY (`hashtag_text`,`tweet_id`),
  ADD KEY `hashtag_text` (`hashtag_text`),
  ADD KEY `tweet_id` (`tweet_id`);

ALTER TABLE `tweet`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `datetime` (`datetime`),
  ADD KEY `lang` (`lang`),
  ADD KEY `in_reply_id` (`in_reply_id`),
  ADD KEY `retweet_id` (`retweet_id`);


ALTER TABLE `hashtag_tweet`
  ADD CONSTRAINT `hashtag_tweet_ibfk_1` FOREIGN KEY (`tweet_id`) REFERENCES `tweet` (`id`);
