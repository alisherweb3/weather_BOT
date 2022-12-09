Почему API это хорошо удобно и популярно?

Давайте я приведу ещё один пример с которым вы сталкивались и никогда не задумывались как оно
работает. Самое первое что приходит на ум это YouTube. А что в нём такого спросите вы А я вам сейчас
расскажу Связь FrontEnd (грубо говоря это всё что вы видите у себя в браузере) и BackEnd(серверная логика) на
YouTube осуществляется с помощью API. Так как YouTube это высоконагруженное приложение то лучше будет
разделить визуальную составляющую и серверную логику,т.е. у каждого пользователя есть свой FromtEnd
который шлёт запрос на сервер с определёнными критериями (например если вы напишете в строке поиска Python 
или перейдёте в какую либо категорию с видео) после того как сервер принял и обработал ваш
запрос(requests) - он отправляет ответ(response) и FrontEnd парсит этот ответ и расставляет его по кусочкам в
необходимые области страницы отображаемой у вас в браузере.

API это к тому же и безопасно так как разработчик сам определяет какой функционал по какому маршруту и
с какими критериями будет доступен, если хоть на чуть чуть отойти от шаблона придуманного
разработчиком, то это приведёт к ошибке, так как сервер не будет знать что же ему делать с запросом не
соответствующим шаблону.

Какие же бывают HTTP запросы?

GET - запрос на получение ресурса. К примеру когда вы обновляете эту страницу ваш браузер посылает GET 
запрос на сервер (sayta)
POST - отправка набора данных к ресурсу. Когда вы вводите логин и пароль для входа на сайт и нажимаете
кнопку войти отправляется POST запрос с данными вашего логина и пароля на сервер.
PUT - имеет схожесть с POST но в отличие от него PUT обновляет данные объекта.
DELETE - удаляет определённый ресурс.
Чаще всего вы будете пользоваться GET и POST запросами