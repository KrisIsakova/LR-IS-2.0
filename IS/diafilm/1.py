import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
import psycopg2
from Glav import Ui_MainWindow
from Dob import Ui_Dialog
from Red import Ui_RedDialog


class DiafilmApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация основного окна
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Загрузка данных в таблицу
        self.load_data()

        # Привязка кнопок к событиям
        self.ui.pushButton_Dob.clicked.connect(self.show_dob_dialog)
        self.ui.pushButton_Red.clicked.connect(self.show_red_dialog)

    def load_data(self):
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname="diafilm",
            user="postgres",
            password="20040214",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Выполнение SQL-запроса для получения данных из таблицы diafilm
        cursor.execute("SELECT * FROM diafilm")
        rows = cursor.fetchall()

        # Установка заголовков столбцов
        headers = ["№ п/п", "Шифр", "Шифр 2", "Шифр 3", "Год на титульнике", "Год на слайде", "Доп. код", "diafilm.su",
                   "diafilm.su 2", "Коробка с этикеткой", "Ссылка на кадр", "Наименование", "Количество экземпляров",
                   "Примечание 1", "Примечание 2"]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        # Установка количества строк в таблице
        self.ui.tableWidget.setRowCount(len(rows))

        # Заполнение таблицы данными
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                # Заменяем None на пустую строку перед добавлением в таблицу
                item_value = str(value) if value is not None else ""
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item_value))

        # Автоматическое изменение ширины столбцов для растягивания по содержимому
        self.ui.tableWidget.resizeColumnsToContents()

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

    def show_dob_dialog(self):
        # Создаем диалоговое окно добавления записи
        dialog = QDialog()
        ui_dob = Ui_Dialog()
        ui_dob.setupUi(dialog)
        dialog.exec_()

    def update_data(self, updated_data, diafilm_number):
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname="diafilm",
            user="postgres",
            password="20040214",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Выводим отладочную информацию перед выполнением SQL-запроса
        print("Updating data in the database...")
        print("Updated data:", updated_data)

        # Обновление данных в базе данных
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

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

        # Выводим сообщение об успешном обновлении данных
        print("Data updated successfully.")

        # Обновление данных в таблице
        self.load_data()

        # Вывод сообщения об успешном обновлении данных
        QMessageBox.information(self, "Успешно", "Данные успешно отредактированы")

    def show_red_dialog(self):
        # Получаем индекс выбранной строки
        selected_row = self.ui.tableWidget.currentRow()

        # Проверяем, выбрана ли строка
        if selected_row != -1:
            # Получаем данные выбранной строки
            selected_data = [self.ui.tableWidget.item(selected_row, i).text() for i in range(self.ui.tableWidget.columnCount())]

            # Создаем диалоговое окно Red
            dialog = QDialog()
            ui_red = Ui_RedDialog()
            ui_red.setupUi(dialog)

            # Заполняем поля в диалоговом окне Red данными из выбранной строки
            for i, data in enumerate(selected_data):
                getattr(ui_red, f"lineEdit_{i + 1}").setText(data)

            # Привязываем функцию сохранения данных к событию нажатия кнопки pushButton_Save
            ui_red.pushButton_Save.clicked.connect(lambda: self.save_data(ui_red, selected_data[0], dialog))

            # Отображаем диалоговое окно
            dialog.exec_()
        else:
            # Если строка не выбрана, выводим сообщение об ошибке
            error_message = "Выберите Диафильм для редактирования"
            QMessageBox.warning(self, "Ошибка", error_message, QMessageBox.Ok)

    def save_data(self, ui_red, diafilm_number, dialog):
        # Получение отредактированных данных из полей диалогового окна
        updated_data = [getattr(ui_red, f"lineEdit_{i + 1}").text() for i in range(15)]

        print("Updated data:", updated_data)  # Добавленная строка для отладки

        # Обновление данных в базе данных без добавления diafilm_number в список
        self.update_data(updated_data, diafilm_number)

        # Закрытие диалогового окна
        dialog.close()


def main():
    app = QApplication(sys.argv)
    window = DiafilmApp()
    window.show()
    exit_code = app.exec_()
    print("Application exited with code:", exit_code)  # Добавленная строка для отладки
    sys.exit(exit_code)



if __name__ == "__main__":
    main()
