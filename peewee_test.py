# pipi install peewee
from models.bookstore import Book, Category
# bookstore모듈을 bs 별칭으로 import
import models.bookstore as bs

# 테이블 생성 테스트 : 모델 매핑 정보를 기반
def create_table_test():
    bs.initialize()

# INSERT와 Relation 테스트
from datetime import datetime
def insert_relation_test():
    # 카테고리 생성
    c1 = bs.insert_category(no=1, name="Python")
    c2 = bs.insert_category(no=2, name="JAVA")

    # Book INSERT
    bs.insert_book(no=1, title="Learning Python", pub_date=datetime(2015, 11, 13), price=10000, category=c1) # c1은 Foreign Key참조
    bs.insert_book(no=2, title="히치하이커 Python", pub_date=datetime(2018, 3, 4), price=18000, category=c1)
    bs.insert_book(no=3, title="Effective JAVA", pub_date=datetime(2013, 7, 8), price=21000, category=c2)
    bs.insert_book(no=4, title="God of JAVA", pub_date=datetime(2008, 1, 15), price=15000, category=c2)

# UPDATE : 별도의 메서드가 있지 않고 get같은 함수를 이용해 메모리에 적재 후 필드를 변경하여 save() 메서드 실행
def update_test():
    # title이 "Effective JAVA"인 책을 찾아와서 가격을 변경
    book = Book.get(Book.title == "Effective JAVA")
    print(book)
    # 업데이트 할 필드를 수정
    book.price += book.price * 0.1 # 가격을 10%인상
    print("업데이트된 Book 객체:", book)
    book.save() # 저장 - > 업데이트

# DELETE : get같은 함수를 이용해 메모리에 적재 후 delete_instance()메서드로 메모리에서 삭제 -> 테이블에서도 삭제
def delete_test():
    book = Book.get(Book.title == "God of JAVA")
    # 메모리에서 삭제 -> 테이블에서도 삭제 가능
    book.delete_instance()

# SELECT
def select_test():
    books = Book.select() # 모든 컬럼 모든 레코드를 추출
    print(books.sql()) # 실제 수행된 SQL 문을 확인할 수 있다
    for book in books:
        print(book)

# SELECT 컬럼의 제한 : Projection
def projection_test():
    # 레코드 추출시 특정 컬럼만 추출할 경우
    # 필요한 필드의 목록을 select() 메서드내에 선언
    books = Book.select(Book.title, Book.price)
    for book in books:
        print("책 제목 {} : {}원".format(book.title, book.price))

# WHERE와 order_by
def where_order_test():
    # 책 가격이 15000원 이상, 가격이 20000원 미만인 모든 책의 목록을 가격의 역순으로 출력
    books = Book.select().where((Book.price>=15000) & (Book.price<20000)).order_by(Book.price.desc())
    print("SQL:", books.sql())
    for book in books:
        print("검색된 책:", book)

# ForeignKeyField 타입으로 작성된 컬럼 타입에 related_name이 설정되어 있다면 PK -> FK 기반으로 역참조가 가능
def reverse_reference_test():
    # 카테고리 내에 포함된 모든 책을 참조
    categories = Category.select()
    for category in categories:
        print("카테고리:", category)
        # related_name에 설정한 이름으로 역참조 가능
        for book in category.books:
            print("카테고리 내의 책들:", book)

if __name__ == "__main__":
    #create_table_test()
    #insert_relation_test()
    #update_test()
    #delete_test()
    #select_test()
    #projection_test()
    #where_order_test()
    reverse_reference_test()