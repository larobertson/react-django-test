# Setting up a virtual environment:

inside of your desired directory:
$ virtualenv -p python3 .

activate it with:
$ source bin/activate

Now you have a fresh environment where you can install dependencies. Check it out using $ pip freeze

You can exit your vitual environment by simply typing deactivate

# To connect PostgreSQL
psycopg2 needs to be installed in order for Django to talk to Postgres.

On Mac: make sure xcode is installed, postgres is installed via homebrew

This gave me trouble. It was solved by looking at pg_config ldflags. Get those like so:
pg_config --ldflags

then inside of the virtual environment run this script:

env LDFLAGS='-L/usr/local/lib -L/usr/local/opt/openssl/lib
-L/usr/local/opt/readline/lib' pip install psycopg2==2.5.2
