#!/bin/bash

commit=false
database_test=false
start=false

for var in "$@"; do
    case $var in
    -c|--commit)
        commit=true
        shift
        shift
        ;;
    -dbt|--database-test)
        database_test=true
        shift
        shift
        ;;
    -s|--start)
        start=true
        shift
        shift
        ;;
    *)
        echo "Unknown argument passed.. '$var'"
        shift
        ;;
    esac
done

if [ "$commit" = true ]; then
    cp src/database.sqlite src/database-base.sqlite
    sqlite3 src/database-base.sqlite "DELETE FROM tokens;"
    git add *
    git commit -m "$1"
    git push
    # echo "Commited code"
fi

if [ "$database_test" = true ]; then
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
    # echo "Database Test"
fi

if [ "$start" = true ]; then
    output="$(ps -aux | grep python3 | grep -v grep)"

    if [[ -n $output ]]; then
        echo "Already running process.."
    else
        cd $HOME/Mona
        git pull
        cd src
        python3 main.py
    fi
fi