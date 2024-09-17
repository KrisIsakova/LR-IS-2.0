import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
import psycopg2
from Glav2 import Ui_MainWindow
from Dob import Ui_DobDialog
from Red import Ui_RedDialog
from avto import Ui_AvtoDialog


class DiafilmApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # загрузка данных в таблицу
        self.load_data()

        # Привязка кнопок
        self.ui.pushButton_Dob.clicked.connect(self.show_dob_dialog)
        self.ui.pushButton_Red.clicked.connect(self.show_red_dialog)
        self.ui.pushButton_Ydal.clicked.connect(self.delete_record)  # Привязка кнопки удаления
        self.ui.pushButton_Poisk.clicked.connect(self.search_data)  # Привязка кнопки поиска
        self.ui.lineEdit_Poisk.textChanged.connect(self.search_data)  # Привязка изменения текста в поле поиска

    def load_data(self):  # вывод данных из бд
        # Подключение к бд
        conn = psycopg2.connect(
            dbname="diafilm",
            user="postgres",
            password="20040214",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # запрос для получения данных из таблицы diafilm
        cursor.execute("SELECT * FROM diafilm")
        rows = cursor.fetchall()

        # заголовки столбцов
        headers = ["№ п/п", "Шифр", "Шифр 2", "Шифр 3", "Год на титульнике", "Год на слайде", "Доп. код", "diafilm.su",
                   "diafilm.su 2", "Коробка с этикеткой", "Ссылка на кадр", "Наименование", "Количество экземпляров",
                   "Примечание 1", "Примечание 2"]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(rows))

        # заполнение таблицы данными
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                # Заменяем None на пустую строку
                item_value = str(value) if value is not None else ""
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item_value))

        # изменение ширины столбцов для растягивания по содержимому
        self.ui.tableWidget.resizeColumnsToContents()

        cursor.close()
        conn.close()

    def show_dob_dialog(self):  # диалоговое окно добавления диафильма
        dialog = DobDialog(self)
        ui_dob = Ui_DobDialog()
        ui_dob.setupUi(dialog)

        ui_dob.pushButton1.clicked.connect(lambda: self.save_new_data(ui_dob, dialog))
        ui_dob.pushButton1_3.clicked.connect(lambda: self.clear_fields(ui_dob))

        dialog.exec_()

    def save_new_data(self, ui_dob, dialog):
        try:
            new_data = [getattr(ui_dob, f"lineEdit_{i + 1}").text() for i in range(15)]
            print("New data to insert:", new_data)

            self.insert_new_data(new_data)
            dialog.close()
        except Exception as e:
            print("An error occurred while saving new data:", e)

    def insert_new_data(self, new_data):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(
                dbname="diafilm",
                user="postgres",
                password="20040214",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()

            print("Inserting new data into the database...")
            print("New data:", new_data)

            cursor.execute("""
                   INSERT INTO diafilm ("number", "cipher", "cipher_2", "cipher_3", "year_on_the_title_card",
                                        "year_on_slide", "add_code", "diafilm.su_1", "diafilm.su_2", "box_with_label",
                                        "frame_link", "name", "copy", "note_1", "note_2")
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, new_data)
            conn.commit()
            print("New data inserted successfully.")

            self.load_data()
            QMessageBox.information(self, "Успешно", "Новая запись успешно добавлена")
        except Exception as e:
            print("An error occurred while inserting new data:", e)
            if conn is not None:
                conn.rollback()
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def update_data(self, updated_data, diafilm_number):
        # Подключение к бд
        conn = psycopg2.connect(
            dbname="diafilm",
            user="postgres",
            password="20040214",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # отклад инфа
        print("Updating data in the database...")
        print("Updated data:", updated_data)

        # Обновляем данные в бд
        try:
            cursor.execute("""
                UPDATE diafilm
                SET
                    "number" = %s,
                    "cipher" = %s,
                    "cipher_2" = %s,
                    "cipher_3" = %s,
                    "year_on_the_title_card" = %s,
                    "year_on_slide" = %s,
                    "add_code" = %s,
                    "diafilm.su_1" = %s,
                    "diafilm.su_2" = %s,
                    "box_with_label" = %s,
                    "frame_link" = %s,
                    "name" = %s,
                    "copy" = %s,
                    "note_1" = %s,
                    "note_2" = %s
                WHERE "number" = %s
            """, updated_data + [diafilm_number])
            conn.commit()
            print("Data updated successfully.")
        except Exception as e:
            print("An error occurred while updating data:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        cursor.close()
        conn.close()

        print("Данные успешно обновились!")

        # Обновление данных в таблице
        self.load_data()

        QMessageBox.information(self, "Успешно", "Данные успешно отредактированы")

    def show_red_dialog(self):
        # Получаем индекс выбранной строки
        selected_row = self.ui.tableWidget.currentRow()

        # Проверка выбрана ли строка
        if selected_row != -1:
            # Получаем данные выбранной строки
            selected_data = [self.ui.tableWidget.item(selected_row, i).text() for i in
                             range(self.ui.tableWidget.columnCount())]

            dialog = RedDialog(self)
            ui_red = Ui_RedDialog()
            ui_red.setupUi(dialog)

            # Заполняем поля по выб строке
            for i, data in enumerate(selected_data):
                getattr(ui_red, f"lineEdit_{i + 1}").setText(data)

            # Привязываем функцию сохранения
            ui_red.pushButton_Save.clicked.connect(lambda: self.save_data(ui_red, selected_data[0], dialog))
            ui_red.pushButton1_3.clicked.connect(lambda: self.clear_fields(ui_red))

            dialog.exec_()
        else:
            error_message = "Выберите Диафильм для редактирования"
            QMessageBox.warning(self, "Ошибка", error_message, QMessageBox.Ok)

    def clear_fields(self, ui):
        for i in range(15):
            getattr(ui, f"lineEdit_{i + 1}").clear()

    def save_data(self, ui_red, diafilm_number, dialog):
        # Получение отредактированных данных
        updated_data = [getattr(ui_red, f"lineEdit_{i + 1}").text() for i in range(15)]

        print("Updated data:", updated_data)  # откладка

        # Обновление данных в бд
        self.update_data(updated_data, diafilm_number)

        dialog.close()

    def delete_record(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            # Получаем номер диафильма для удаления
            diafilm_number = self.ui.tableWidget.item(selected_row, 0).text()

            # Выводим сообщение с подтверждением перед удалением
            reply = QMessageBox.question(self, 'Подтверждение удаления',
                                         "Вы уверены, что хотите удалить данный диафильм?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Подключение к бд
                conn = psycopg2.connect(
                    dbname="diafilm",
                    user="postgres",
                    password="20040214",
                    host="localhost",
                    port="5432"
                )
                cursor = conn.cursor()

                try:
                    cursor.execute("DELETE FROM diafilm WHERE number = %s", (diafilm_number,))
                    conn.commit()
                    self.ui.tableWidget.removeRow(selected_row)
                    QMessageBox.information(self, "Успешно", "Запись успешно удалена")
                except Exception as e:
                    print("An error occurred while deleting the record:", e)
                    conn.rollback()
                finally:
                    cursor.close()
                    conn.close()
            else:
                # Если пользователь отказался от удаления, просто игнорируем
                pass
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для удаления", QMessageBox.Ok)

    def search_data(self):
        search_text = self.ui.lineEdit_Poisk.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            match = False
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column)
                if item is not None and search_text in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget.setRowHidden(row, not match)


class AvtoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AvtoDialog()
        self.ui.setupUi(self)

        self.ui.pushButton1_2.clicked.connect(self.check_credentials)

    def check_credentials(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "1" and password == "1":
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль", QMessageBox.Ok)


class DobDialog(QDialog):
    def __init__(self, parent=None):
        super(DobDialog, self).__init__(parent)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение',
                                     "Вы уверены, что хотите закрыть окно Добавления?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class RedDialog(QDialog):
    def __init__(self, parent=None):
        super(RedDialog, self).__init__(parent)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение',
                                     "Вы уверены, что хотите закрыть окно Редактирования?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)

    login_dialog = AvtoDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        window = DiafilmApp()
        window.show()
        exit_code = app.exec_()
        print("Application exited with code:", exit_code)
        sys.exit(exit_code)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
