import psycopg2


class Pg_manager:

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.cursor = self.connect()

        self.query = ""


    def connect(self):
        connection = psycopg2.connect(host=self.host, database=self.database,
                            user=self.user, password=self.password, port=self.port)
        connection.autocommit = True
        cursor = connection.cursor()

        return cursor


    def selectInitie(self, title):
        self.cursor.execute("""SELECT answer FROM initie WHERE title = \'""" + self.escapedChar(title) + """\'""")
        return self.cursor.fetchone()


    def insertInitie(self, title, answer):
        self.cursor.execute("""INSERT INTO initie(title, answer, dateadded) VALUES(\'""" + self.escapedChar(title) + """\', \'""" + self.escapedChar(answer) + """\', NOW())""")


    def insertReplyofBot(self, reply, *argv):
        if reply == "0":
            self.cursor.execute("""INSERT INTO replyofbot(reply, datereplied) VALUES(\'""" + reply + """\', NOW())""")
        else:
            self.cursor.execute("""INSERT INTO replyofbot(reply, datereplied, title, answer) VALUES(\'""" + reply + """\', NOW(), \'""" + self.escapedChar(argv[0]) + """\', \'""" + self.escapedChar(argv[1]) + """\')""")    

    
    def escapedChar(self, s):
        return s.replace("'", "\'\'")