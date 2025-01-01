from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QTableWidget, QHeaderView, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIcon, QColor, QPainter, QPixmap
###
from connection_ui import Ui_dlgConnection
from registration_ui import Ui_MainWindow
from finalize_order_ui import Ui_FinalizeOrder
###
from database import DataBase
from decimal import Decimal
from datetime import datetime
import pyodbc
import sys
global connection, myCursor

##########################################################################
# DATABASE CONNECTION WINDOW
class ConnectionDialog(QDialog, Ui_dlgConnection):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Management System - Login")
        appIcon = QIcon(':icons/assets/python-icon.png')
        self.setWindowIcon(appIcon)
##########################################################################

##########################################################################
# FINALIZE ORDER WINDOW
class FinalizeOrderDialog(QDialog, Ui_FinalizeOrder):
    def __init__(self, selected_products, product_values, cpf_tel_name_balance):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Management System - Finish")
        appIcon = QIcon(':icons/assets/python-icon.png')
        self.setWindowIcon(appIcon)
        
        self.selected_products = selected_products
        self.product_values = product_values
        self.cpf_tel_name_balance = cpf_tel_name_balance

        self.tbl_finalized_products.verticalHeader().setVisible(False)
        self.product_names = self.selected_products.keys()
        self.product_quantities = self.selected_products.values()

        self.ProductId = []
        self.product_price = []
        # UPDATE TABLE
        self.update_finalized_products_table()
        self.update_edit_fields()
        self.update_account_data()
        

        # BUTTONS
        self.btn_order_finalized.clicked.connect(self.finalize_order)
        self.btn_customer_value.clicked.connect(self.customer_value)

    def calculate_price(self):
        db = DataBase()
        db.connect()

        for i, j in enumerate(self.product_names):
            current_id = db.get_product_id(j)
            self.ProductId.append(current_id)
            current_price = db.get_product_price(current_id)
            self.product_price.append(current_price)

        db.close_connection()


    def update_finalized_products_table(self):
        self.calculate_price()
        self.tbl_finalized_products.setRowCount(len(self.selected_products))
        row = 0

        for product, quantity in self.selected_products.items():
            product_item = QTableWidgetItem(product)
            quantity_item = QTableWidgetItem(str(quantity))
            
            self.tbl_finalized_products.setItem(row, 0, product_item)
            self.tbl_finalized_products.setItem(row, 1, quantity_item)
            
            row += 1

        row = 0
        for price in self.product_price:

            price_item = QTableWidgetItem(str(price))
            self.tbl_finalized_products.setItem(row, 2, price_item)
            row += 1

    def update_edit_fields(self):
        
        subtotal = str(sum(self.product_values))
        
        self.edit_subtotal.setText(subtotal)
        self.edit_total_paid.setText(subtotal)
        
        

    def customer_value(self):

        if len(self.edit_customer_value.text()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Value not informed!")
            msg.setText("Value not informed, try again!")
            msg.exec()
        else:
            if self.edit_customer_value.text().strip() == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Value not informed!")
                msg.setText("Only spaces were informed, try again!")
                msg.exec()
            else:

                subtotal = float(self.edit_subtotal.text().replace(',', '.'))
                if ',' in self.edit_customer_value.text():
                    customer_value = float(self.edit_customer_value.text().replace(',', '.'))
                    
                else:
                    customer_value = float(self.edit_customer_value.text())
                
                change = customer_value - subtotal
                change_text = str(change).replace('.', ',')
                self.edit_change.setText(change_text)
                self.edit_total_paid.setText(str(customer_value).replace('.', ','))




    def update_account_data(self):

        if self.cpf_tel_name_balance != 'ERROR':
             
            for i, data in enumerate(self.cpf_tel_name_balance):
                if i == 0:

                    self.edit_cpf_account.setText(str(data))
                elif i == 1:

                    self.edit_phone_account.setText(str(data))
                elif i == 2:

                    self.edit_name_account.setText(str(data))
                else:

                    self.edit_balance_account.setText(str(data))
        else:

            self.edit_cpf_account.setText('Cpf - account not informed')
            self.edit_phone_account.setText('Phone - account not informed')
            self.edit_name_account.setText('Name - account not informed')     
            self.edit_balance_account.setText('Balance - account not informed')




    def finalize_order(self):
        db = DataBase()
        db.connect()

        error = ''

        # INSERT ORDER DATA
        try:

            # CHECK IF THERE IS A ACCOUNT IN THE ORDER
            try:
                cpf = int(self.edit_cpf_account.text())
                account_id = db.get_account_id(cpf)
            except:
                account_id = None


            order_date = datetime.now()

            order_value = float(self.edit_subtotal.text().replace(',', '.'))

            amount_paid = float(self.edit_total_paid.text().replace(',', '.'))

            change_value = float(self.edit_change.text().replace(',', '.'))

            full_data_set = (
                order_date,
                order_value,
                amount_paid,
                change_value
            )

            res = db.register_order(full_data_set)

            if res == 'ERROR':
                print('ERROR!!!')
            


        except pyodbc.Error as e:
            error = e
            print('ERROR WHILE REGISTERING ORDER!', e)
            


        # INSERT ORDER ITEM DATA
        try:
            order_id = db.get_last_order_id()

            product_ids = self.ProductId.copy()
            product_quantities = list(self.product_quantities)

            for i, j in enumerate(product_ids):
                product_id = j
                product_quantity = product_quantities[i]
                full_data_set = (
                    order_id,
                    product_id,
                    product_quantity,
                )
                db.register_order_item(full_data_set)

        except pyodbc.Error as e:
            error += ' ' + e
            print('ERROR WHILE REGISTERING ORDER ITEM: ', e)



        # INSERT DATA INTO THE CASH REGISTER
        try:

            previous_balance = float(db.get_cash_balance())

            # USING THE VARIABLES DEFINED EARLIER
            closing_balance = previous_balance + order_value

            full_data_set = (
                order_date,
                previous_balance,
                closing_balance
            )

            response = db.register_cash(full_data_set)
        except pyodbc.Error as e:
            error += ' ' + e
            print('ERROR WHILE INSERTING DATA INTO THE CASH REGISTER!')



        # INSERT CUSTOMER ACCOUNT DATA IF EXISTS
        try:
            if account_id is not None:

                balance = db.get_account_balance(account_id)

                new_balance = float(balance) - order_value

                db.update_account_balance(account_id, new_balance)

            else:
                pass
        except pyodbc.Error as e:
            error += ' ' + e

        db.close_connection()

        if error == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Order")
            msg.setText("Order successfully completed")
            msg.exec()
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERROR")
            msg.setText("Error completing the order correctly!")
            msg.exec()
            self.close()


##########################################################################



##########################################################################
# MAIN WINDOW
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tbl_selected_products.verticalHeader().setVisible(False)
        self.setWindowTitle("Management System")
        appIcon = QIcon(':icons/assets/python-icon.png')
        self.setWindowIcon(appIcon)

        ################################################
        # LEFT MENU BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)
        ################################################


        ################################################
        # ADJUST THE SIDE SPACE OF COLUMNS IN THE CASH TABLE
        header = self.tbl_cash.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(150)
        ################################################


        ######################################################
        # MAIN PAGES OF THE SYSTEM
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_accounts.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_register))
        self.btn_products.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_products))
        self.btn_order.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_order))
        self.btn_cash.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cash))
        self.btn_about.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))
        ######################################################

        ######################################################
        # PRODUCT CATEGORIES PAGE IN THE ORDER PAGE pg_order
        self.btn_snacks.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_snacks))
        self.btn_drinks.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_drinks))
        self.btn_sandwiches.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_sandwiches))
        self.btn_sweets.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_sweets))
        self.btn_sodas.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_sodas))
        self.btn_specials.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_specials))
        self.btn_products_home.clicked.connect(lambda: self.ProductTypes.setCurrentWidget(self.pg_products_home))
        ######################################################

        ######################################################
        # PRODUCT CATEGORIES PAGES IN THE PRODUCTS PAGE pg_products
        self.btn_snacks2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_snacks2))
        self.btn_drinks2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_drinks2))
        self.btn_sandwiches2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_sandwiches2))
        self.btn_sweets2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_sweets2))
        self.btn_sodas2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_sodas2))
        self.btn_specials2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_specials2))
        self.btn_products_home2.clicked.connect(lambda: self.ProductTypes2.setCurrentWidget(self.pg_products_home2))
        ######################################################

        ######################################################
        # CONFIGURING THE SELECTED PRODUCTS IN THE ORDER
        self.selected_products = {}

        # CREATING THE LISTS FOR PRODUCTS
        self.product_names = []
        self.product_quantities = []
        self.product_ids = []
        self.product_values = []

        # SNACKS
        self.btn_coxinha.clicked.connect(lambda: self.add_selected_product("Coxinha", 1))
        self.btn_sfiha.clicked.connect(lambda: self.add_selected_product("Sfiha /Chicken", 1))
        self.btn_burger.clicked.connect(lambda: self.add_selected_product("Burger", 1))
        self.btn_croissant.clicked.connect(lambda: self.add_selected_product("Croissant", 1))
        self.btn_pao_de_queijo.clicked.connect(lambda: self.add_selected_product("Cheese Bread", 1))

        # DRINKS
        self.btn_water.clicked.connect(lambda: self.add_selected_product("Mineral Water", 1))
        self.btn_dellvale.clicked.connect(lambda: self.add_selected_product("DellVale Juice", 1))
        self.btn_tea_lipton.clicked.connect(lambda: self.add_selected_product("Lipton Tea", 1))
        self.btn_tea_matte.clicked.connect(lambda: self.add_selected_product("Matte Tea", 1))

        # SANDWICHES
        self.btn_hamburger.clicked.connect(lambda: self.add_selected_product("Hamburger", 1))
        self.btn_grilled_cheese.clicked.connect(lambda: self.add_selected_product("Grilled Cheese", 1))

        # SWEETS
        self.btn_lollipop.clicked.connect(lambda: self.add_selected_product("7Belo Lollipop", 1))
        self.btn_candy_azedinho.clicked.connect(lambda: self.add_selected_product("Candy Azedinho", 1))
        self.btn_mentos.clicked.connect(lambda: self.add_selected_product("Mentos", 1))

        # SODAS
        self.btn_coca_cola.clicked.connect(lambda: self.add_selected_product("Coca-Cola", 1))
        self.btn_coca_cola_zero.clicked.connect(lambda: self.add_selected_product("Coca-Cola Zero", 1))
        self.btn_guarana.clicked.connect(lambda: self.add_selected_product("Guarana", 1))
        self.btn_guarana_zero.clicked.connect(lambda: self.add_selected_product("Guarana Zero", 1))
        self.btn_orange_fanta.clicked.connect(lambda: self.add_selected_product("Orange Fanta", 1))

        # SPECIALS
        self.btn_hot_dog.clicked.connect(lambda: self.add_selected_product("Hot Dog", 1))
        self.btn_pastel.clicked.connect(lambda: self.add_selected_product("Pastel", 1))
        ######################################################

        ######################################################
        # BUTTONS TO INCREASE OR DECREASE THE QUANTITY OF SELECTED PRODUCT
        self.btn_increase_1.clicked.connect(lambda: self.change_quantity(1))
        self.btn_increase_2.clicked.connect(lambda: self.change_quantity(2))
        self.btn_decrease_1.clicked.connect(lambda: self.change_quantity(-1))
        self.btn_decrease_2.clicked.connect(lambda: self.change_quantity(-2))
        ######################################################

        ######################################################
        # BUTTON TO DELETE PRODUCT FROM THE DICTIONARY
        self.btn_delete_product.clicked.connect(self.delete_product)
        ######################################################

        ######################################################
        # BUTTON TO DELETE ALL PRODUCTS FROM THE ORDER
        self.btn_cancel_order.clicked.connect(self.cancel_order)
        ######################################################

        ######################################################
        # BUTTON TO FINALIZE ORDER BY OPENING THE FINALIZE ORDER WINDOW
        self.btn_finalize_order.clicked.connect(self.finalize_order)
        ######################################################

        ######################################################
        # BUTTON TO EXIT
        self.btn_exit.clicked.connect(self.close_window)
        ######################################################


        ###############################################################################################
        # BUTTONS FOR THE ACCOUNT TABLE
        self.btn_register.clicked.connect(self.register_account)
        self.btn_update_account.clicked.connect(self.update_account)
        self.btn_delete_account.clicked.connect(self.delete_account)

        self.btn_confirm_account.clicked.connect(self.search_account_info)

        # UPDATE TABLES
        self.search_account()
        self.search_cash()
        self.search_order()
        self.search_order_item()

        ###############################################################################################


        ##################################################################
        # STORE ACCOUNT INFO IN ORDER
        self.account_info = []
        ##################################################################

        ##################################################################
        # IMAGE CANTEEN LOGO PAINT TO ADAPT SIZE
        self.image = QPixmap(":/icons/assets/canteen-logo.png")
        ##################################################################

    ###############################################################################################
    # METHODS TO WORK WITH ORDER

    def calculate_value(self):
        db = DataBase()
        db.connect()

        self.product_names = list(self.selected_products.keys())
        self.product_quantities = list(self.selected_products.values())

        unit_price = []
        for product_name in self.product_names:
            product_id = db.get_product_id(product_name)
            unit_price_value = db.get_product_price(product_id)
            unit_price.append(unit_price_value)

        self.product_prices = []
        for i, quantity in enumerate(self.product_quantities):
            total_product_value = quantity * unit_price[i]
            self.product_prices.append(total_product_value)

        total_sum = sum(self.product_prices)
        self.edit_total_value.setText(str(total_sum))

        # WHEN THE DECIMAL SEPARATOR IS ',' INSTEAD OF '.'
        # self.edit_total_value.setText(str(total_sum).replace('.', ','))

        db.close_connection()


    def update_finalized_products_table(self):
        pass
    

    def add_selected_product(self, product_name, quantity):
        if product_name in self.selected_products:
            self.selected_products[product_name] += quantity
        else:
            self.selected_products[product_name] = quantity
        
        self.update_selected_products_table()
        self.update_total_quantity()


    def update_selected_products_table(self):
        self.tbl_selected_products.setRowCount(len(self.selected_products))
        row = 0
        total_quantity = 0  
        for product, quantity in self.selected_products.items():
            product_item = QTableWidgetItem(product)
            quantity_item = QTableWidgetItem(str(quantity))
            self.tbl_selected_products.setItem(row, 0, product_item)
            self.tbl_selected_products.setItem(row, 1, quantity_item)
            row += 1
            total_quantity += quantity

        self.calculate_value()
        self.edit_item_quantity.setText(str(total_quantity))
        


    def change_quantity(self, increment):
        
        row = self.tbl_selected_products.currentRow()

        if row != -1:
            product_item = self.tbl_selected_products.item(row, 0)
            quantity_item = self.tbl_selected_products.item(row, 1)
            
            if product_item is not None and quantity_item is not None:
                product = product_item.text()
                current_quantity = int(quantity_item.text())
                new_quantity = current_quantity + increment

                if new_quantity > 0:
                    quantity_item.setText(str(new_quantity))
                    self.selected_products[product] = new_quantity
                else:
                    product = product_item.text()
                    
                    self.tbl_selected_products.removeRow(row)
                    del self.selected_products[product]

        self.update_selected_products_table()
        self.update_total_quantity()

    def delete_product(self):
        row = self.tbl_selected_products.currentRow()

        if row != -1:
            product_item = self.tbl_selected_products.item(row, 0)
            
            if product_item is not None:
                product = product_item.text()
                self.tbl_selected_products.removeRow(row)
                del self.selected_products[product]

            # <...>
            self.update_selected_products_table()
            self.update_total_quantity()

    def cancel_order(self):
        self.selected_products = {}
        self.update_selected_products_table()
        self.edit_item_quantity.setText('0')


    def update_total_quantity(self):
        total_quantity = sum(self.selected_products.values())
        self.edit_item_quantity.setText(str(total_quantity))


    def search_account_info(self):
        db = DataBase()
        db.connect()
        cpf = self.edit_account_cpf.text()
        if cpf.isnumeric():
            cpf = int(self.edit_account_cpf.text())

            result = db.get_account(cpf)

            if result is None or result == []:
                self.edit_account_cpf.setText('')
                self.edit_account_phone.setText('')
                self.edit_account_name.setText('')
                self.edit_account_balance.setText('')
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR")
                msg_box.setText("Error identifying the account! Please try again.")
                msg_box.setStyleSheet("QMessageBox { background-color: white; }"
                                    "QMessageBox QLabel { color: red; background-color: transparent;}"
                                    "QMessageBox QPushButton { background-color: white;}")
                msg_box.exec()

            else:
                values = list(result[0])

                if isinstance(values[-1], Decimal):
                    values[-1] = float(values[-1])

                values = [int(v) if isinstance(v, (int, float)) else v for v in values]

                for i, j in enumerate(values):
                    if i == 0:
                        self.edit_account_cpf.setText(str(j))
                    elif i == 1:
                        self.edit_account_phone.setText(str(j))
                    elif i == 2:
                        self.edit_account_name.setText(j)
                    else:
                        self.edit_account_balance.setText(str(j))

                self.info = values.copy()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Account Error")
            msg.setText("Error identifying the account, please select only numbers!")
            msg.exec()

    def finalize_order(self):
        if self.selected_products:
            
            dialog = FinalizeOrderDialog(self.selected_products, self.product_prices, self.account_info)
            dialog.exec()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("No product selected")
            msg_box.setText("Please select at least one product before finalizing the order.")
            msg_box.setStyleSheet("QMessageBox { background-color: white; }"
                                "QMessageBox QLabel { color: red; background-color: transparent;}"
                                "QMessageBox QPushButton { background-color: white;}")
            msg_box.exec()

        # CLEAR FIELDS
        self.edit_item_quantity.setText('0')
        self.edit_total_value.setText('0.00')
        self.edit_account_cpf.clear()
        self.edit_account_phone.clear()
        self.edit_account_name.clear()
        self.edit_account_balance.clear()
        self.tbl_selected_products.clearContents()
        self.tbl_selected_products.setRowCount(0)
        self.selected_products = {}

        # UPDATE TABLES
        self.search_account()
        self.search_cash()
        self.search_order()
        self.search_order_item()


    ###############################################################################################




    ###############################################################################################
    # METHOD FOR LATERAL MENU TRANSITION
    def leftMenu(self):

        width = self.left_menu.width()

        if width == 9:
            newWidth = 100
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    ###############################################################################################

    ##########################################################################
    # METHOD TO SEARCH CASH REGISTER
    def search_cash(self):
        db = DataBase()
        db.connect()
        box_data = db.get_all_cash_data()

        self.tbl_cash.clearContents()
        self.tbl_cash.setRowCount(len(box_data))

        for row, text in enumerate(box_data):
            for column, data in enumerate(text):
                if column == 0:
                    box_id = str(data)
                    self.tbl_cash.setItem(row, column, QTableWidgetItem(box_id))
                elif column == 1:
                    box_date = str(data)
                    self.tbl_cash.setItem(row, column, QTableWidgetItem(box_date))
                elif column == 2:
                    opening_balance = float(data)
                    self.tbl_cash.setItem(row, column, QTableWidgetItem(str(opening_balance)))
                elif column == 3:
                    closing_balance = float(data)
                    self.tbl_cash.setItem(row, column, QTableWidgetItem(str(closing_balance)))

        db.close_connection()


    def search_order(self):
        db = DataBase()
        db.connect()
        order_data = db.get_all_orders()

        self.tbl_orders.clearContents()
        self.tbl_orders.setRowCount(len(order_data))

        for row, text in enumerate(order_data):
            for column, data in enumerate(text):
                if column == 0:
                    order_id = str(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(order_id))
                elif column == 1:
                    account_id = str(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(account_id))
                elif column == 2:
                    order_date = str(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(order_date))
                elif column == 3:
                    order_value = float(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(str(order_value)))
                elif column == 4:
                    paid_value = float(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(str(paid_value)))
                else:
                    change_value = float(data)
                    self.tbl_orders.setItem(row, column, QTableWidgetItem(str(change_value)))

        db.close_connection()


    def search_order_item(self):
        db = DataBase()
        db.connect()
        order_item_data = db.get_all_order_items()

        self.tbl_order_item.clearContents()
        self.tbl_order_item.setRowCount(len(order_item_data))

        for row, text in enumerate(order_item_data):
            for column, data in enumerate(text):
                if column == 0:
                    order_id = str(data)
                    self.tbl_order_item.setItem(row, column, QTableWidgetItem(order_id))
                elif column == 1:
                    product_name = db.get_product_name(data)
                    self.tbl_order_item.setItem(row, column, QTableWidgetItem(product_name))
                elif column == 2:
                    quantity = str(data)
                    self.tbl_order_item.setItem(row, column, QTableWidgetItem(quantity))

        db.close_connection()

    ###############################################################################################
    # METHODS FOR HANDLING ACCOUNTS

    def register_account(self):
        db = DataBase()
        db.connect()
        
        try:
            int_cpf = int(self.txt_cpf.text())
            int_phone = int(self.txt_phone.text())

            if '.' in self.txt_value.text():
                float_value = float(self.txt_value.text())
            else:
                float_value = float(self.txt_value.text().replace(',', '.'))

            full_data_set = (
            self.txt_name.text(),
            int_cpf,
            self.txt_email.text(),
            int_phone,
            float_value
            )
            resp = db.register_account(full_data_set)

            if resp == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Registration Successful")
                msg.setText("Account successfully registered")
                msg.exec()
                db.close_connection()

                self.search_account()
                self.txt_name.clear()
                self.txt_cpf.clear()
                self.txt_email.clear()
                self.txt_phone.clear()
                self.txt_value.clear()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Error registering account, could not complete the registration!")
                msg.exec()
                db.close_connection()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Data Error")
            msg.setText("Error registering account, please check if the information was entered correctly!")
            msg.exec()
            db.close_connection()


    def search_account(self):

        db = DataBase()
        db.connect()
        result = db.get_all_accounts()

        self.tbl_accounts.clearContents()
        self.tbl_accounts.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                if column == 5:
                    balance_txt = str(data).replace('.', ',')
                    self.tbl_accounts.setItem(row, column, QTableWidgetItem(balance_txt))
                else:        
                    self.tbl_accounts.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()


    def delete_account(self):

        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("This record will be deleted.")
        msg.setInformativeText("Are you sure you want to delete?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            account_id = self.tbl_accounts.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_account(account_id)
            self.search_account()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("ACCOUNTS")
            msg.setText(result)
            msg.exec()

        db.close_connection()


    def update_account(self):

        rows = self.tbl_accounts.rowCount()
        columns = self.tbl_accounts.columnCount()

        data = []

        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = self.tbl_accounts.item(row, col)
                if item is not None:
                    if col in [1, 3]:
                        value = item.text()
                    elif col in [0, 2, 4]:
                        if col == 0:
                            first = int(item.text())
                        else:
                            value = int(item.text())
                    elif col == 5:
                        if ',' in item.text():
                            value = float(item.text().replace(',', '.'))
                        else:
                            value = float(item.text())

                    if col != 0:  
                        row_data.append(value)
            row_data.append(first)
                        
            data.append(tuple(row_data))

        # UPDATE DATA IN DATABASE
        db = DataBase()
        db.connect()

        # UPDATE DATA IN DATABASE
        resp = db.update_account(data)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Update Successful")
            msg.setText("The account has been successfully updated.")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Error updating account. Please check if the information was entered correctly.")
            msg.exec()

        db.close_connection()

    ###############################################################################################

    ##########################################################################
    # METHOD TO CLOSE WINDOW USING btn_exit BUTTON
    def close_window(self):
        self.close()

    ##########################################################################


##########################################################################
# INITIALIZER
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    dlgCon = ConnectionDialog() 
    while True:
        if dlgCon.exec() == QDialog.Accepted: 
            try: 
                connection = pyodbc.connect(driver="SQL Server", 
                                    server=f"{dlgCon.edServer.text()}", 
                                    database=f"{dlgCon.edDatabase.text()}", 
                                    uid=f"{dlgCon.edUser.text()}", 
                                    pwd=f"{dlgCon.edPassword.text()}") 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Successful Connection")
                msg.setText("Connection was successfully established!")
                msg.exec()
                myCursor = connection.cursor()
                window = MainWindow() 
                window.show()
                app.exec()
                break  
            except pyodbc.Error as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("ERROR - TRY AGAIN")
                msg.setText(f"COULD NOT ESTABLISH CONNECTION! \n[ERROR] - {e}")
                msg.exec()
        else:
            break
##########################################################################