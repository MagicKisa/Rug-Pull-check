# Rug-Pull-check
it's about save people from scam in crypto.

Целью данной работы является продукт который позволяет как создателям криптовалюты так и её покупателям иметь возможность проводить более прозрачные сделки.

Machine Learning будет использоваться для определения некоторых закономерностей в мошеннической деятельности в децентрализованных системах, чтобы благодаря ним предупреждать действия недобросовестных разработчиков, и защищать честную работу людей.

Я считаю это поможет людям в финансовом плане, что в целом улучшит жизнь на нашей планете.(Может звучит очень пафосно😊)

Сбор данных - это первый и критически важный этап в нашем проекте по прогнозированию мошеннических криптовалют. На этом этапе мы должны собрать как можно больше данных о различных криптовалютах, включая их транзакционную историю, характеристики блокчейна, информацию о командах разработчиков и другие связанные атрибуты. Эти данные будут нашими основными входами для обучения и проверки моделей машинного обучения.

Немного о DxSale – это площадка предназначенная для запуска криптовалют – одна из многих, при просмотре первой страницы можно заметить, что сайт активен, и запускающиеся сейчас криптовалюты имеют инвесторов (один из таких проектов https://dx.app/dxsaleview?saleID=270&chain=BNB собрал 400 bnb на данный момент – речь идёт о 80.000$)

## I Источники данных

***1.	DxSale.app***
-	Названия уже запущенных и запускающихся криптовалют
-	Адреса создателя токена, самого токена в сети блокчейн bnb, которые можно просматривать на bscscan.com
-	Ссылки на контакты разработчиков криптовалют в социальных сетях	
Существуют и другие (https://trustpad.io/?g=ended&p=0 ) платформы запуска(их называют launchpad), и при недостатке информации можно обратиться к ним. На этой платформе 224 монеты на данный момент, которые в среднем набирают меньше денег чем launchpad binance (1mln bnb) и больше чем https://bscpad.com/ (5 bnb)

***2.	Bscscan.com***
-	Все операции по криптовалюте
-	Код криптовалюты
-	Все адреса связанные с этими операциями
-	Капитализация токена

Бесплатный сервис для просмотра всех операций в Blockain-сети Bsc.

***3.	Telegram.org (как и другие социальные сети)***
-	Существование чатов и каналов разработчиков

Многие монеты не имеют канала в телеграмм, поэтому стоит обратить внимание на иные социальные сети

Все источники предоставляют актуальные данные и работают на момент написания этого текста.

## II API

Источники 1-2 предоставляют API через Get

Некоторые примеры запросов на

***DxSale***

https://scan.dx.app/api/v2/sales/offChain/successfulSales?page=2
данный Get запрос предоставляет json с успешными сделками (2-ю страницу)

***Bscscan***

https://api.bscscan.com/api?module=contract&action=getsourcecode&address=0xa29685F043A89998eA18254e8E450Df989E13e2b&apikey=myapikey

Предоставляет код смартконтракта

***Telegram*** 

предоставляет API через бота. С помощью скрипта tg.py (В приложении) можно узнать существует ли канал, более подробную информацию получить без согласия администратора нельзя. На скриншоте результат выполнения скрипта.
 


