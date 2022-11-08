# @author = "Feng Xinyu"
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QDialog,
                             QTableWidget, QLineEdit, QPushButton,
                             QMessageBox, QTableWidgetItem, QHeaderView)


class SignIn(QDialog):
    """
        登录页
    """

    import pymysql
    # 全局账号密码字典（管理员为admin，普通用户递增字符串）
    # 账户，用户名，密码(账户唯一，作为键)
    # user_password_dic = {"root": ['admin', '123456'],
    #                      "1": ['zhangsan', ''],
    #                      "2": ['lisi', '123456'],
    #                      "3": ['lisi', '123456']}

    login_user_name = ''  # 天鸣
    login_id = ''

    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)
        self.init_ui()

    # 1.布局部分
    def init_ui(self):
        self.resize(220, 330)
        self.setWindowTitle("图书管理系统")

        # Pixmap,142,184
        pixmap = QPixmap(r"C:\Users\Feng Xinyu\Desktop\pic1.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.move(39, 15)

        # label_username
        label_username = QLabel(self)
        label_username.setText("用户名：")
        label_username.move(50, 210)

        # label_password
        label_password = QLabel(self)
        label_password.setText("密码：")
        label_password.move(50, 240)

        # line_edit_username
        self.line_edit_username = QLineEdit(self)
        self.line_edit_username.resize(80, 20)
        self.line_edit_username.move(100, 208)

        # line_edit_password
        self.line_edit_password = QLineEdit(self)
        self.line_edit_password.resize(80, 20)
        self.line_edit_password.move(100, 238)
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        # button_sign_in
        button_sign_in = QPushButton("登录", self)
        button_sign_in.move(74, 280)

        # label_author
        label_author = QLabel(self)
        label_author.setText("冯新宇")
        label_author.move(172, 310)

        # 调用
        button_sign_in.clicked.connect(self.sign_in)

        self.show()

    # TODO 2.交互部分
    def sign_in(self):

        # 用于判断登录的str
        # global str_user_name, str_password
        str_user_name = self.line_edit_username.text()
        str_password = self.line_edit_password.text()

        print("username:", str_user_name)
        print("password:", str_password)

        # TODO 调用user_id
        conn = SignIn.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # 查询用户
                sql = f'select * from `user_information`;'
                cursor.execute(sql)
                datas = cursor.fetchall()
                print(datas)
        except Exception as e:
            pass
        finally:
            conn.close()

        print("用户ID：", datas)

        # TODO 判断登录逻辑
        for i in datas:
            if str_user_name == i[0]:
                print("用户名存在，为", str_user_name)
                # 先判断密码是否正确
                if str_password == i[2]:
                    print("密码正确")
                    # 进一步判断用户类型
                    if str_user_name == 'root':
                        print("管理员账户")
                        # TODO 管理员界面，进入管理页
                        self.hide()
                        self.enter_the_management_interface = ManagementInterface()
                    else:
                        print("普通用户")
                        SignIn.login_user_name = i[1]
                        SignIn.login_id = str_user_name
                        # TODO 个人信息，进入已借阅图书详情页
                        self.hide()
                        self.get_into = BorrowedBooks()
                        # self.get_into.show()
                else:
                    print("密码错误")
                break
        else:
            print("用户名不存在，请重新输入")


class ManagementInterface(QWidget):  # 管理端界面：可供实现用户管理，图书管理，增删改查等
    """
        管理端界面
    """

    def __init__(self):
        super(ManagementInterface, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 1.布局部分
        self.resize(200, 200)
        self.setWindowTitle("管理端界面")

        # TODO user_managerment_button
        user_managerment_button = QPushButton("用户管理", self)
        # user_managerment_button.setWindowTitle("用户管理")
        user_managerment_button.move(60, 50)
        user_managerment_button.clicked.connect(self.get_into_user_management)

        # TODO book_managerment_button
        book_managerment_button = QPushButton("图书管理", self)
        book_managerment_button.move(60, 100)
        book_managerment_button.clicked.connect(self.get_into_book_management)

        self.show()

    def get_into_user_management(self):
        # self.hide()
        # self.exec_()
        self.get_into = UserManagerment()

    def get_into_book_management(self):
        self.get_into = BookManagerment()


class UserManagerment(QWidget):
    """
        管理端：用户管理
    """
    import pymysql

    def __init__(self, parent=None):
        super(UserManagerment, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.resize(300, 320)
        self.setWindowTitle("用户管理")

        # label_user_id
        label_user_id = QLabel("用户ID：", self)
        label_user_id.move(50, 50)

        # label_user_name
        label_user_name = QLabel("用户名称：", self)
        label_user_name.move(50, 100)

        # label_user_password
        label_user_password = QLabel("用户密码：", self)
        label_user_password.move(50, 150)

        # label_repeat_password
        label_repeat_password = QLabel("重复密码：", self)
        label_repeat_password.move(50, 200)

        # line_edit_uesr_id
        self.line_edit_user_id = QLineEdit(self)
        self.line_edit_user_id.move(130, 50)
        # TODO 设定默认值
        # self.line_edit_user_id.setText("ccc")

        # line_edit_user_name
        self.line_edit_user_name = QLineEdit(self)
        self.line_edit_user_name.move(130, 100)

        # line_edit_user_password
        self.line_edit_user_password = QLineEdit(self)
        self.line_edit_user_password.move(130, 150)
        self.line_edit_user_password.setEchoMode(QLineEdit.Password)

        # line_edit_repeat_password
        self.line_edit_repeat_password = QLineEdit(self)
        self.line_edit_repeat_password.move(130, 200)
        self.line_edit_repeat_password.setEchoMode(QLineEdit.Password)

        # button_create_user
        button_create_user = QPushButton("创建用户", self)
        button_create_user.move(26, 250)
        button_create_user.clicked.connect(self.create_user)

        # button_modify_user
        button_modify_user = QPushButton("修改用户", self)
        button_modify_user.move(114, 250)
        button_modify_user.clicked.connect(self.modify_user)

        # button_modify_password
        button_modify_password = QPushButton("修改密码", self)
        button_modify_password.move(202, 250)

        # button_select_user
        button_select_user = QPushButton("查询用户", self)
        button_select_user.move(26, 280)
        button_select_user.clicked.connect(self.select_user)

        # button_delete_user
        button_delete_user = QPushButton("删除用户", self)
        button_delete_user.move(114, 280)
        button_delete_user.clicked.connect(self.delete_user)

        # button_return_to_root
        button_return_to_root = QPushButton("返回", self)
        button_return_to_root.move(202, 280)

        self.show()

    def create_user(self):
        str_user_id = self.line_edit_user_id.text()
        str_user_name = self.line_edit_user_name.text()
        str_user_password = self.line_edit_user_password.text()
        str_repeat_password = self.line_edit_repeat_password.text()

        # 先判断是否全部输入了内容
        if (len(str_user_id) > 0) and (len(str_user_name) > 0) and (len(str_user_password) > 0) and (
                len(str_repeat_password) > 0):
            print("全部输入有效")
            # TODO 查询数据库，来判断是否存在已知账户
            conn = UserManagerment.pymysql.connect(host='localhost',
                                                   user='root',
                                                   port=3306,
                                                   password='123456',
                                                   db="library_management_system",
                                                   charset='utf8'
                                                   )
            try:
                with conn.cursor() as cursor:
                    # 准备SQL语句
                    sql = "select student_id from user_information;"
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 执行完SQL语句后的返回结果都是保存在cursor中
                    # 所以要从cursor中获取全部数据
                    datas = cursor.fetchall()
                    print("获取的数据：\n", datas)
            except Exception as e:
                print("数据库操作异常：\n", e)
            finally:
                # 不管成功还是失败，都要关闭数据库连接
                conn.close()
            print(datas)

            # 遍历查找
            for i in datas:
                # print(i[0])
                if str_user_id == i[0]:
                    print("账户存在，无法创建")
                    break
            else:
                # TODO 执行数据录入，判断字符串规则

                # TODO 判断输入的两个密码是否相同
                if str_user_password == str_repeat_password:
                    print("可以创建此账户")
                    conn = UserManagerment.pymysql.connect(
                        host='localhost',
                        user='root',
                        port=3306,
                        password='123456',
                        db="library_management_system",
                        charset='utf8'
                    )
                    try:
                        with conn.cursor() as cursor:
                            # 创建用户语句
                            sql = f'INSERT INTO `user_information` VALUES ' \
                                  f'("{str_user_id}", "{str_user_name}","{str_user_password}");'
                            # sql = 'select * from user_information;'
                            cursor.execute(sql)
                            # 执行完要提交
                            conn.commit()
                            print("添加用户成功")
                            # TODO 显示一下
                    except Exception as e:
                        # 如果执行失败要回滚
                        conn.rollback()
                        print("数据库操作异常：\n", e)
                    finally:
                        # 不管成功还是失败，都要关闭数据库连接
                        conn.close()
                else:
                    print("输出的两次密码不相同，请重新输入")

    def modify_user(self):
        # TODO 修改用户逻辑
        str_user_id = self.line_edit_user_id.text()
        str_user_name = self.line_edit_user_name.text()

        if len(str_user_id) > 0:  # and (len(str_user_name) > 0):
            print("输入值有效")
            # TODO 调用数据库查询是否存在已知账户
            conn = UserManagerment.pymysql.connect(host='localhost',
                                                   user='root',
                                                   port=3306,
                                                   password='123456',
                                                   db="library_management_system",
                                                   charset='utf8'
                                                   )
            try:
                with conn.cursor() as cursor:
                    # 准备SQL语句
                    sql = "select student_id from user_information;"
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 执行完SQL语句后的返回结果都是保存在cursor中
                    # 所以要从cursor中获取全部数据
                    datas = cursor.fetchall()
                    print("获取的数据：\n", datas)
            except Exception as e:
                print("数据库操作异常：\n", e)
            finally:
                # 不管成功还是失败，都要关闭数据库连接
                conn.close()
            print(datas)

            # 遍历查找
            for i in datas:
                # print(i[0])
                if str_user_id == i[0]:
                    # TODO
                    print("账户存在，修改名称")
                    conn = UserManagerment.pymysql.connect(host='localhost',
                                                           user='root',
                                                           port=3306,
                                                           password='123456',
                                                           db="library_management_system",
                                                           charset='utf8'
                                                           )
                    try:
                        with conn.cursor() as cursor:
                            sql = f'UPDATE `user_information` SET `user_name`="{str_user_name}" WHERE `student_id`="{str_user_id}";'
                            cursor.execute(sql)
                            conn.commit()
                            print("修改用户名成功")
                            # TODO 显示一下
                    except Exception as e:
                        # 如果执行失败要回滚
                        conn.rollback()
                        print("数据库操作异常：\n", e)
                    finally:
                        conn.close()
                    break
            else:
                print("账户不存在")

    def modify_password(self):
        # TODO 修改密码逻辑，密码修改完成后清除密码框
        pass

    def select_user(self):
        # TODO 查询用户逻辑：通过用户ID查询用户名称、密码
        str_user_id = self.line_edit_user_id.text()
        # print(type(str_user_id))
        if len(str_user_id) > 0:
            print("输入有效")
            # self.line_edit_user_name.setText("ttt")
            # 连接数据库
            conn = UserManagerment.pymysql.connect(host='localhost',
                                                   user='root',
                                                   port=3306,
                                                   password='123456',
                                                   db="library_management_system",
                                                   charset='utf8'
                                                   )
            # noinspection PyBroadException
            try:
                with conn.cursor() as cursor:
                    # 准备数据库语句
                    sql = f'SELECT * FROM `user_information` WHERE `student_id`="{str_user_id}";'
                    cursor.execute(sql)
                    datas = cursor.fetchall()
                    # print(len(datas))
                    if len(datas) == 0:
                        print("账户不存在")
                        # TODO 跳出？
                    else:
                        str_user_name = datas[0][1]
                        str_password = datas[0][2]
                        self.line_edit_user_name.setText(str_user_name)
                        self.line_edit_user_password.setText(str_password)  # TODO 密码看不见
                        QMessageBox.information(self, "提示", f"用户ID：{str_user_id}\n"
                                                            f"用户名称：{str_user_name}\n"
                                                            f"密码：{str_password}")
                    print("获取的数据：\n", datas)
            except Exception as e:
                print("数据库操作异常：\n", datas)
            finally:
                conn.close()
            print(datas)
        else:
            print("请输入内容")

    def delete_user(self):
        # TODO 删除用户逻辑
        # TODO 1.先查询用户借阅表是否有已经借阅的书籍
        str_user_id = self.line_edit_user_id.text()

        conn = UserBookOperation.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # TODO sql语句，查询输入的用户是否存在已借阅的书籍
                sql = f'SELECT COUNT(*) ' \
                      f'FROM `user_borrow_book` ' \
                      f'WHERE `student_id`="{str_user_id}";'
                cursor.execute(sql)
                num_borrowed_book = cursor.fetchall()
        except Exception as e:
            pass
        finally:
            conn.close()
        print("已借阅书籍数量：", num_borrowed_book[0][0])

        print("====================分割线====================")

        # TODO 2.通过用户ID删除用户（不能删除管理员用户，不能删除已借阅书籍的用户）
        if str_user_id == "root":
            print("是管理员，无法删除。")
        else:
            if int(num_borrowed_book[0][0]) == 0:
                # TODO 删除用户操作
                print("可以删除用户...")
                conn = UserManagerment.pymysql.connect(host='localhost',
                                                       user='root',
                                                       port=3306,
                                                       password='123456',
                                                       db="library_management_system",
                                                       charset='utf8'
                                                       )
                try:
                    with conn.cursor() as cursor:
                        # SQL语句，删除用户
                        sql = f'DELETE FROM `user_information` ' \
                              f'WHERE `student_id`="{str_user_id}";'
                        cursor.execute(sql)
                        conn.commit()
                        print("删除用户成功")
                except Exception as e:
                    # 如果执行失败要回滚
                    conn.rollback()
                    print("数据库操作异常：\n", e)
                finally:
                    conn.close()
            else:
                print("存在已经借阅的书，无法删除用户。")


class BookManagerment(QWidget):
    """
        管理端：图书管理
    """

    def __init__(self, parent=None):
        super(BookManagerment, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.resize(350, 260)
        self.setWindowTitle("图书管理")

        # label_all_books_borrowed
        label_all_books_borrowed = QLabel(self)
        label_all_books_borrowed.setText("已借阅的所有书籍")
        label_all_books_borrowed.move(10, 10)

        t = self.get_all_borrowing_information()
        x = len(t)

        # table_column_name
        self.table_column_name = QTableWidget(x, 4, self)
        # 适应内容的宽度，无法手动调整宽度
        self.table_column_name.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_column_name.setHorizontalHeaderLabels(["借阅人", "书名", "ISBN", "借阅时间"])
        # 单元格默认宽度为100px 高30px 两边编号以及拖动条和的宽度为30px 去掉单元格后高40px
        self.table_column_name.resize(330, 190)
        self.table_column_name.move(10, 30)

        # 添加数据到表格
        for i in range(x):
            for j in range(4):
                print(i, j)
                item = QTableWidgetItem(str(t[i][j]))
                print(str(t[i][j]))
                # print(item)
                self.table_column_name.setItem(i, j, item)

        # TODO 归还部分界面
        # label_num_of_returned_books
        num_of_returned_books = QLabel(self)
        num_of_returned_books.setText("请输入归还书籍的编号：")
        num_of_returned_books.move(10, 234)

        # line_num_of_returned_books
        self.line_edit_num_of_returned_books = QLineEdit(self)
        self.line_edit_num_of_returned_books.resize(90, 20)
        self.line_edit_num_of_returned_books.move(150, 230)

        # button_return_books
        self.button_return_books = QPushButton("归还图书", self)
        self.button_return_books.move(245, 230)

        self.show()

    @staticmethod
    def get_all_borrowing_information():
        # TODO 获取所有的借阅信息
        conn = BorrowedBooks.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # TODO 查询所有借阅信息
                sql = "SELECT * FROM `user_borrow_book`;"
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as e:
            print("数据库操作异常：\n", e)
        finally:
            conn.close()
        print("管理端，所有借阅的书籍：", data)
        return data

    # TODO 归还逻辑部分
    # 注：归还涉及2张表操作，注意回滚


class BorrowedBooks(QWidget):  # 个人借阅信息：普通用户进入的界面，交互已解决
    """
        已经借阅的图书
    """
    import pymysql

    def __init__(self):
        super(BorrowedBooks, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 1.布局部分
        self.resize(380, 500)
        self.setWindowTitle("个人借阅图书查询/详情")

        # label_student_name
        label_student_name = QLabel(self)
        label_student_name.setText("姓名：")
        label_student_name.move(60, 50)

        # label_print_student_name
        self.label_print_student_name = QLabel(self)
        # label_print_student_name.setText("冯新宇")
        # TODO 遗留的问题
        # print(SignIn.sign_in().str_user_name)
        # self.label_print_student_name.setText("aaa")
        self.label_print_student_name.setText(SignIn.login_user_name)  # 天鸣
        self.label_print_student_name.move(100, 50)

        # label_student_id
        label_student_id = QLabel(self)
        label_student_id.setText("学号：")
        label_student_id.move(60, 80)

        # label_print_student_id
        self.label_print_student_id = QLabel(self)
        self.label_print_student_id.setText(SignIn.login_id)
        self.label_print_student_id.move(100, 80)

        # TODO label_number_of_books_borrowed
        label_number_of_books_borrowed = QLabel(self)
        label_number_of_books_borrowed.setText("已借阅数量：")
        label_number_of_books_borrowed.move(25, 110)

        # TODO 获取借阅的数据书籍的数量
        self.num_borrowed_books = self.return_borrowing_number()
        print("借阅数量：", self.num_borrowed_books)

        # TODO 获取借阅的书的信息
        self.information_borrowed_books = self.get_borrowing_information()
        print("num_borrowed_books:", self.information_borrowed_books)

        self.label_print_number_of_books_borrowed = QLabel(self)
        self.label_print_number_of_books_borrowed.setText(str(self.num_borrowed_books))  # todo why?
        self.label_print_number_of_books_borrowed.move(100, 110)

        # label_detailed
        label_detailed = QLabel(self)
        label_detailed.setText("详细：")
        label_detailed.move(60, 140)

        # label_print_detailed
        self.label_print_detailed = QTableWidget(5, 2, self)
        self.label_print_detailed.setHorizontalHeaderLabels(["名称", "借阅时间"])
        self.label_print_detailed.resize(230, 190)
        self.label_print_detailed.move(100, 140)

        # button_return
        self.button_return = QPushButton("返回", self)
        self.button_return.move(60, 400)
        # 调用：返回上一级界面
        self.button_return.clicked.connect(self.return_sign_in)

        # button_into_borrow_return
        self.button_into_borrow_return = QPushButton("进入书库", self)
        self.button_into_borrow_return.move(200, 400)
        self.button_into_borrow_return.clicked.connect(self.enter_the_library)

        # line_edit_return_book_num：归还书籍输入的编号
        self.line_edit_return_book_num = QLineEdit(self)
        self.line_edit_return_book_num.resize(100, 30)
        self.line_edit_return_book_num.move(60, 360)

        # button_return_book
        self.button_return_book = QPushButton("归还", self)
        self.button_return_book.move(200, 360)
        self.button_return_book.clicked.connect(self.return_book)

        # 添加数据到表格：已借阅的书籍
        for i in range(len(self.information_borrowed_books)):
            print(i)
            item = QTableWidgetItem(self.information_borrowed_books[i][0])
            # print(item)
            self.label_print_detailed.setItem(i, 0, item)

        self.show()

    # TODO 2.交互
    def return_sign_in(self):
        # my = SignIn(self)
        # my.mySignal.connect(self.setText)
        # my.exec_()

        self.hide()
        # my.hide()

        self.return_to_homepage = SignIn()
        # self.return_to_homepage.show()

    def enter_the_library(self):
        # 进入书库
        # self.hide()
        self.into_borrow_return_interface = UserBookOperation()

    @staticmethod
    def get_borrowing_information():
        # 返回借阅信息
        conn = BorrowedBooks.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        try:
            with conn.cursor() as cursor:
                # TODO 统计用户借阅的所有书
                student_id = SignIn.login_id  # todo 获取的用户ID
                sql = f'SELECT book_name FROM `user_borrow_book` WHERE `student_id`="{student_id}";'
                cursor.execute(sql)
                data = cursor.fetchall()
                print("查询成功")
                print("书籍详情信息：", data)
        except Exception as e:
            print("数据库操作异常：\n", e)
        finally:
            conn.close()
        return data

    @staticmethod
    def return_borrowing_number():
        # 返回借阅数量
        conn = BorrowedBooks.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # TODO 统计当前用户借阅的书的数量
                student_id = SignIn.login_id
                print("student_id：", student_id)
                sql = f'SELECT COUNT(*) FROM `user_borrow_book` WHERE `student_id`="{student_id}";'
                cursor.execute(sql)
                data = cursor.fetchall()
                print("数量详情")
        except Exception as e:
            print("数据库操作异常")
        finally:
            conn.close()
        return str(data[0][0])

    def return_book(self):
        # TODO 还书功能
        # TODO 1.获取 information_borrowed_books
        print(self.information_borrowed_books)
        # TODO 2.获取输入框的内容
        # line_edit_return_book_num
        self.num_return_book_num = self.line_edit_return_book_num.text()
        print("类型：", type(self.num_return_book_num))
        print("长度：", len(self.num_return_book_num))
        print(self.num_return_book_num)
        # TODO 3.判断输入值是否在范围内
        t = len(self.information_borrowed_books)  # 已借阅书籍数量
        if self.num_return_book_num.isdigit():
            print("是纯数字")
            int_book_row_num = int(self.num_return_book_num) - 1  # 获取下标
            if (int_book_row_num >= 0) and (int_book_row_num < t):  # 判断下标位置
                print("再范围内")
                # TODO 4.归还操作，归还的书编号有了，已借阅的书有了，需要先获取库存
                # TODO 获取库存部分
                conn = UserBookOperation.pymysql.connect(
                    host='localhost',
                    user='root',
                    port=3306,
                    password='123456',
                    db="library_management_system",
                    charset='utf8'
                )
                # noinspection PyBroadException
                try:
                    with conn.cursor() as cursor:
                        # TODO 查询库存
                        book_name = self.information_borrowed_books[int_book_row_num][0]
                        sql = f'SELECT `stock` FROM `book_information` ' \
                              f'WHERE `name`="{book_name}";'
                        cursor.execute(sql)
                        stock_data = cursor.fetchall()
                except Exception as e:
                    pass
                finally:
                    conn.close()
                print("现有的库存：", stock_data[0][0])

                # TODO 归还操作部分
                conn = UserBookOperation.pymysql.connect(
                    host='localhost',
                    user='root',
                    port=3306,
                    password='123456',
                    db="library_management_system",
                    charset='utf8'
                )
                # noinspection PyBroadException

                try:
                    with conn.cursor() as cursor:
                        # TODO sql语句，删除已经借阅的书籍信息，添加库存信息
                        sql = f'DELETE FROM `user_borrow_book` WHERE ' \
                              f'(`student_id`="{SignIn.login_id}" AND ' \
                              f'`book_name`="{book_name}");'
                        cursor.execute(sql)

                        # 库存 + 1 ---> str
                        stock_new = str(int(stock_data[0][0]) + 1)
                        sql = f'UPDATE `book_information` ' \
                              f'SET `stock`="{stock_new}" ' \
                              f'WHERE `name`="{book_name}";'
                        cursor.execute(sql)

                        conn.commit()
                        print("归还成功")
                except Exception as e:
                    conn.rollback()
                    print("数据库操作异常：\n", e)
                finally:
                    conn.close()
            else:
                print("越界了")
        else:
            print("不是纯数字")


class UserBookOperation(QWidget):
    """
        用户借阅归还书籍在这里
    """
    import pymysql

    def __init__(self):
        super(UserBookOperation, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 1.布局部分
        self.resize(250, 500)
        self.setWindowTitle("用户借阅归还界面")

        # label_book_name
        lable_book_name = QLabel(self)
        lable_book_name.setText("请输入借阅书籍的编号：")
        lable_book_name.move(50, 350)

        # line_edit_book_row_num
        self.line_edit_book_row_num = QLineEdit(self)
        self.line_edit_book_row_num.resize(100, 20)
        self.line_edit_book_row_num.move(50, 370)

        # button_borrow
        self.button_borrow = QPushButton("借阅", self)
        self.button_borrow.move(50, 410)
        self.button_borrow.clicked.connect(self.row_num_borrow_books)

        # TODO 获取库存量
        self.stock = self.get_inventory()

        # table_widget_stock
        self.table_widget_stock = QTableWidget(len(self.stock), 2, self)
        self.table_widget_stock.setHorizontalHeaderLabels(["名称", "库存"])
        self.table_widget_stock.resize(230, 320)
        self.table_widget_stock.move(10, 10)

        print(self.stock[0][1])

        # TODO 添加数据
        for i in range(len(self.stock)):
            for j in range(2):
                print(i, j)
                item = QTableWidgetItem(str(self.stock[i][j]))  # 字符串？
                # item = self.stock[i][j]
                # print(item)
                self.table_widget_stock.setItem(i, j, item)

        self.show()

    @staticmethod
    def get_inventory():
        # 获取库存量
        conn = UserBookOperation.pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db="library_management_system",
            charset='utf8'
        )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # 查询库存
                sql = f'SELECT `name`,`stock` FROM `book_information`;'
                cursor.execute(sql)
                datas = cursor.fetchall()
                print(datas)
        except Exception as e:
            pass
        finally:
            conn.close()
        print("库存量：", datas)

        return datas

    def row_num_borrow_books(self):
        # 按照编号的方式借阅书籍
        str_book_row_num = self.line_edit_book_row_num.text()  # 获取编号字符串

        if str_book_row_num.isdigit():  # 判断是否为纯数字
            # TODO 借阅书籍操作核心：库存为零已判定，可借阅多本（尚未处理）
            int_book_row_num = int(str_book_row_num) - 1  # 获取下标
            # print(int_book_row_num)
            print("是纯数字")
            book_information = self.get_inventory()
            # print(book_information[int_book_row_num][0])  # TODO 书名
            t = len(book_information)  # 获取书籍编号长度
            if (int_book_row_num >= 0) and (int_book_row_num < t):  # 判断下标位置
                print("在范围内")
                # TODO 判断书库是否为零
                if int(book_information[int_book_row_num][1]) > 0:  # 判断所剩书籍够不够
                    print("余量充足")
                    # TODO 需要获取用户id ---> user_id int_book_row_num book_information
                    user_id = SignIn.login_id
                    # TODO 判断书籍是否已经借阅
                    # TODO
                    conn = UserBookOperation.pymysql.connect(
                        host='localhost',
                        user='root',
                        port=3306,
                        password='123456',
                        db="library_management_system",
                        charset='utf8'
                    )
                    # noinspection PyBroadException
                    try:
                        with conn.cursor() as cursor:
                            # TODO sql语句，查询已借阅的书籍
                            book_name = book_information[int_book_row_num][0]
                            sql = f'SELECT COUNT(*) FROM `user_borrow_book` WHERE ' \
                                  f'(`student_id`="{user_id}" AND`book_name`="{book_name}");'
                            cursor.execute(sql)
                            datas = cursor.fetchall()
                    except Exception as e:
                        pass
                    finally:
                        conn.close()
                    print("已查询借阅书籍：", datas[0][0])  # TODO 大于零为已借阅，等于零为未借阅

                    print("====================分割线====================")

                    if int(datas[0][0]) == 0:
                        new_stock = book_information[int_book_row_num][1] - 1  # 借一次书，减一次1
                        conn = UserBookOperation.pymysql.connect(
                            host='localhost',
                            user='root',
                            port=3306,
                            password='123456',
                            db="library_management_system",
                            charset='utf8'
                        )
                        try:
                            with conn.cursor() as cursor:
                                # TODO sql语句：借阅书籍
                                sql = f'update `book_information` set `stock`="{new_stock}" ' \
                                      f'where `name`="{book_information[int_book_row_num][0]}";'
                                cursor.execute(sql)

                                sql = f'INSERT INTO `user_borrow_book` VALUES ' \
                                      f'("{user_id}","{book_information[int_book_row_num][0]}",NULL,NULL);'
                                cursor.execute(sql)

                                conn.commit()
                                print("借阅成功")
                        except Exception as e:
                            conn.rollback()
                            print("数据库操作异常：\n", e)
                        finally:
                            conn.close()
                    else:
                        print("已借阅")
                else:
                    print("书不够了")
            else:
                print("越界啦")
        else:
            print("请重新输入编号")


class BookDetailedInformation(QWidget):
    '''
        书籍详情信息
    '''

    def __init__(self):
        super().__init__()
        self.init_ui()

    import pymysql

    @staticmethod
    def try_():
        conn = BookDetailedInformation.pymysql.connect(host='localhost',
                                                       user='root',
                                                       port=3306,
                                                       password='123456',
                                                       db="library_management_system",
                                                       charset='utf8'
                                                       )
        # noinspection PyBroadException
        try:
            with conn.cursor() as cursor:
                # sql = 'show databases;'
                # cursor.execute(sql)
                # cursor.fetchall()
                sql = 'select * from book_information where `name`="python study";'
                cursor.execute(sql)
                datas = cursor.fetchall()
                print("表名：", datas)

        except Exception as e:
            print("数据库异常：\n", e)
        finally:
            conn.close()
        return datas[0][0]

    def init_ui(self):
        self.resize(300, 300)
        self.setWindowTitle("书籍详情页")

        # label_book_name
        self.label_book_name = QLabel(self)
        # label_book_name.setText("名称：")
        # TODO 尝试
        self.label_book_name.setText(self.try_())
        self.label_book_name.move(50, 80)

        # label_author
        label_author = QLabel(self)
        label_author.setText("作者：")
        label_author.move(50, 110)

        # label_ISBN
        label_isbn = QLabel(self)
        label_isbn.setText("ISBN号：")
        label_isbn.move(50, 140)

        # label_stock
        label_stock = QLabel(self)
        label_stock.setText("图书剩余数量：")
        label_stock.move(50, 170)

        self.show()


class DatabaseCall:
    """
        待定，未修改
    """

    @staticmethod
    def books_borrowed_by_current_user(a="ttt"):
        # TODO 统计当前用户借阅的所有书
        return a + "bbb"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = SignIn()
    # start = ManagementInterface()
    # start = userManagerment()
    # start = bookManagerment() # 还没写
    # start = BorrowedBooks()
    # start = UserBookOperation()
    # start = BookDetailedInformation()
    sys.exit(app.exec_())
