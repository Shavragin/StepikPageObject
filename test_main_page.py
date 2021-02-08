from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйверав Url адрес
    page.open() #открываем страницу
    page.go_to_login_page() #Выполняем метод страницы - переходим на страницу логина