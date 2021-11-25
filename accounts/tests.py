from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import os


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # ドライバーのパスは適宜修正
        cls.selenium = WebDriver(
            executable_path='../../opt/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページ
        self.selenium.get('http://localhost:8000' +
                          str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys(os.environ.get('TEST_USER'))
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(os.environ.get('TEST_PASS'))
        self.selenium.find_element_by_class_name('btn').click()

        # ページタイトル検証
        self.assertEquals('日記一覧 | Private Diary', self.selenium.title)
