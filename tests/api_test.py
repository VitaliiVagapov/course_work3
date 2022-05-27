from run import app

class TestApi:

    def test_app_all_post_status_code(self):
        """Проверка на получение нормального списка"""
        response = app.test_client().get('/api/posts', fullow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"


    def test_app_one_post_status_code(self):
        """Проверка на получение нормального списка"""
        response = app.test_client().get('/api/posts/1', fullow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
