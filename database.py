# import dependencies
import sqlite3

# create a connection to a database
conn = sqlite3.connect('database.sqlite')

# database about books/movies
cursor = conn.cursor()

# write our create table statements
script_one = """

drop table if exists objects;

create table objects (
id integer primary key,
author text not null,
language text not null,
title text not null
);

insert into objects (id,author,language,title)
values (1,'jones','test','poop'),
        (2,'jack','yoo','poop'),
        (3,'jerk','yoo','poop');
"""

# now let's execute this query
cursor.executescript(script_one)

# and commit
conn.commit()

# and close
conn.close()