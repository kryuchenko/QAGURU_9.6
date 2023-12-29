from datetime import time


def test_dark_theme_by_time():
    try:
        # Пример: текущее время установлено на 23:00
        current_time = time(hour=23)
        # Реализация логики переключения на темную тему
        if 22 <= current_time.hour or current_time.hour < 6:
            is_dark_theme = True
        else:
            is_dark_theme = False

        # Проверка корректности темы в зависимости от времени
        if 22 <= current_time.hour or current_time.hour < 6:
            assert is_dark_theme is True, "Должна быть активна темная тема, но она не активна."
        else:
            assert is_dark_theme is False, "Должна быть активна дневная тема, но это не так."

    except Exception as e:
        # Обработка любых неожиданных исключений
        print(f"Произошла ошибка: {e}")


def test_dark_theme_by_time_and_user_choice():
    if dark_theme_enabled_by_user is None:
        # Переключаем тему в зависимости от времени суток
        if current_time.hour >= 18 or current_time.hour < 6:
            is_dark_theme = True  # Темная тема ночью
        else:
            is_dark_theme = False  # Светлая тема днем
    else:
        # Пользовательский выбор имеет приоритет
        is_dark_theme = dark_theme_enabled_by_user
    return is_dark_theme


current_time = time(hour=20)  # Например, 20:00
dark_theme_enabled_by_user = None  # Пользователь не сделал выбор


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = next((user for user in users if user["name"] == "Olga"), None)
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def read_func(func, *args, **kwargs):
    func_name = func.__name__.replace("_", " ").title()
    args_str = ", ".join(map(str, args))
    kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    all_args = ', '.join(filter(None, [args_str, kwargs_str]))
    print(f"{func_name} [{all_args}]")
    return f"{func_name} [{all_args}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = read_func(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = read_func(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = read_func(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
