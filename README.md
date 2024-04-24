## Проект UI автотестов IVI


<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/jira.png"></code>
  <code><img width="5%" title="Postman" src="images/postman.png"></code>
</p>


<!-- Тест кейсы -->

### Будет протестирована главная страница сайта ИВИ, а также основные функциональности, переходы по разделам, соответствие текста в разделах наименованию раздела:
* тестирование кликабельности кнопки Войти 
* тестирование перехода в Каталог Мультфильмы, соответствие содержимого раздела наименованию 
* тестирование раздела уведомлений: корректный переход, ожидаемый текст 
* тестирование поля поиска на главной странице
* тестирование видимости кнопки "Смотреть 30 дней бесплатно" при выполнении определенных условий



<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

##### Результаты тестов можно посмотреть в Allure отчете, откуда можно перейти и в Jenkins, где можно самостоятельно запустить сборку
![This is an image](images/Allure_report_web.png)

##### Вкладка Graphs полезна для того, чтобы посмотреть графики о прохождении тестов.
![This is an image](images/Allure_graphs.png)

##### Во вкладке Suites можно найти тест кейсы, в каждом из которых описаны шаги, а также приложени attachments: видео, скрины, фото, логи
![This is an image](images/Allure_suites.png)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/4138/dashboards)

##### Более наглядная отчетность находится в Allure TestOps.
![This is an image](images/Allure_testops_report.png)

#### Сьюты содержат в себе:
- Тест-кейсы
- Интеграция с Jira

![This is an image](images/Allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Интеграция с Jira
##### С помощью Allure TestOps можно направлять отчет в Jira

![This is an image](images/Jira_report.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/telega.png"> Интеграция с Telegram
##### В Telegram bot приходит сообщение с результатами тестирования.

![This is an image](images/telegram.png)
