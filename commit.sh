#!/bin/bash
cp src/database.sqlite src/database-base.sqlite
sqlite3 src/database-base.sqlite "DELETE FROM tokens;"
git add *
git commit -m "$1"
git push

#Build sqlite table for testing...
sqlite3 src/database-test.sqlite ""
sqlite3 src/database-test.sqlite "CREATE TABLE tokens(id integer primary key autoincrement, name text, token text, url_ref text);"
sqlite3 src/database-test.sqlite "CREATE TABLE event_view(id integer primary key autoincrement, name text, guild_id text)"
sqlite3 src/database-test.sqlite "CREATE TABLE event_history(id integer primary key autoincrement, event_type int, guild_id text, channel_id text, is_voice_channel bool, is_private_message bool, date datetime)"
sqlite3 src/database-test.sqlite "CREATE TABLE server_info(id text, owner_id text, splash text, banner text, icon text)"
sqlite3 src/database-test.sqlite "CREATE TABLE channel_info(id text, guild_id text, name text, position int, created_at datetime)"
sqlite3 src/database-test.sqlite "CREATE TABLE messages(id text, guild_id text, channel_id text, author_id text, created_at datetime, content text)"
sqlite3 src/database-test.sqlite "CREATE TABLE aliases(id integer primary key autoincrement, guild_id text, alias text, response text)"
sqlite3 src/database-test.sqlite "CREATE TABLE user_activity(id integer primary key autoincrement, activity_name text, game_name text, start text, ref_url text)"
