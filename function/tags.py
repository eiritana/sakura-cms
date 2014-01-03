"""Generate links and indexes for tags.

%%func tags some_tag another_tag%%

"""


from sakura import common
from cStringIO import StringIO
from bs4 import BeautifulSoup
from page_meta import page_meta
from sakura.common import ini
import sqlite3 as sqlite


SAKURA_ARGS = ['document_path', 'document']  # i wanna rename document to contents


def tags(document_path, document, *args):
    # check/setup tables in sqlite db
    conn = sqlite.connect('database/tags.db')
    cursor = conn.cursor()
    sql = '''
          CREATE TABLE IF NOT EXISTS article (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            href TEXT NOT NULL UNIQUE
          );

          CREATE TABLE IF NOT EXISTS tag (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
          );

          CREATE TABLE IF NOT EXISTS article_tag (
            article_id INTEGER REFERENCES article(id),
            tag_id INTEGER REFERENCES tag(id),

            PRIMARY KEY (article_id, tag_id)
          );
          '''
    cursor.executescript(sql)
    document_directory, __ = document_path.rsplit('/', 1)(document_directory)
    settings = ini('blog_index')
    soup = BeautifulSoup(article)

    # article table: article_id, title, href
    title_element = soup.find(id=(settings['title']['id'],))
    title = title_element.contents[0]
    href = path.split('/', 1)[-1]
    sql = 'INSERT INTO article (title, href) VALUES (?, ?)'
    cursor.execute(sql, (title, href))

    # assure tags in db
    for tag in args:
        cursor.execute('INSERT INTO tag (name) VALUES (?)', (tag,))

    # link tabs to article in db
    sql = 'SELECT id FROM article WHERE href=?'
    article_id = cursor.fetchone(sql, (href,))[0]

    for tag in args:
        sql = 'INSERT INTO article_tag (article_id, tag_id)'
        cursor.execute(sql, (article_id, tag))

    cursor.execute('SELECT id, name FROM tag')
    tags_to_index = cursor.fetchall()

    for tag_id, tag_name in tags_to_index:
        index_html = StringIO()

        # now select href to article and lookup all articles matching tag_id
        pass

    return contents.getvalue()
