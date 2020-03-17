import sqlite3

# db를 연결받아서 __init__에서 판단, None이 아니면 -> open -> __init__에서 open에서 설정한 conn과 cursor값 세팅
class Database:
    # 생성자 : __init__
    def __init__(self, db=None): # 만약 db파라미터가 안넘어오면 db가 세팅되어있지않다고 판단
        # 객체 내부에서 사용할 conn, cursor 객체를 초기화
        self.conn = None
        self.cursor = None
        # 만약 인자로 db정보가 넘어오면 open 수행
        if db:
            self.open(db)

    def open(self, db): # 커넥션 생성
        # 예외처리
        try :
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database 접속 실패")

    def close(self): # 접속 해제 메서드
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    # with문과 함께 사용되는 라이프 사이클 메서드 : __enter__, __exit__
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with 블록이 끝날 때 호출, conn 닫기
        self.close()

    # SELECT 수행용 메서드
    def execute_select(self, sql, parameter=None): # 파라미터가 있을 것을 대비해서 None으로 설정
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else: #파라미터가 없는 경우
            self.cursor.execute(sql)
        data = list(self.cursor.fetchall())
        return data

    # INSERT, UPDATE, DELETE 수행용 메서드
    def execute_cud(self, sql, parameter=None):
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else:
            self.cursor.execute(sql)