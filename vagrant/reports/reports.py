import psycopg2
from datetime import datetime

def get_popular_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # c.execute("select title, count(path) as hits from articles, log where substring(path,10) = slug "
    #           "group by title order by hits desc limit 3")


    # CHOOSE TO USE VIEWS OR DON'T. BUT MAKE A DECISION.


    c.execute("select * from articlehits order by hits desc limit 3")
    top_articles = c.fetchall()
    print(top_articles)
    db.close()
    log_file = open("logfile.txt", "a")
    report_head = "3 MOST POPULAR ARTICLES - {0}".format(datetime.now())
    articles_report = "1. \"{0}\" - {1} views \r\n2. \"{2}\" - {3} views \r\n3. \"{4}\" - {5} views\r\n"\
        .format(top_articles[0][0],
                str(top_articles[0][1]),
                top_articles[1][0],
                str(top_articles[1][1]),
                top_articles[2][0],
                str(top_articles[2][1]))
    print(articles_report)
    log_file.write(report_head+"\r\n--------------------------------------------------\r\n")
    log_file.write(articles_report)
    log_file.close()
    return top_articles

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    content = bleach.clean(content)
    c.execute("insert into posts values (%s)", (content,))
    db.commit()
    db.close()
    # POSTS.append((content, datetime.datetime.now()))

get_popular_articles()


