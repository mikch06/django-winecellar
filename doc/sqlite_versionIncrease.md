#### Increase sqlite version on CentOS
    # Get the current sqlite version on CentOS:
    cd /tmp
    wget https://www.sqlite.org/2019/sqlite-tools-linux-x86-3300100.zip
    unzip sqlite-tools-linux-x86-3300100.zip
    which sqlite3
    cd /tmp/sqlite-tools-linux-x86-3300100
    cp sqlite3 /usr/bin/sqlite3

    yum install glibc.i686
    yum -y install libz.so.1

    # Check:
    sqlite3
    SQLite version 3.30.1 2019-10-10 20:19:45