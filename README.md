# A Python Tor template on Gitpod

Это шаблон, настроенный для временных сред разработки на [Gitpod](https://www.gitpod.io/).

## Prebuild
[![prebuild](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#prebuild/https://github.com/easy-quest/template-pw)


## Начало работы с собственным проектом
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/easy-quest/template-pw)



### Новый проект

Нажмите на кнопку выше  "Open in Gitpod"  , чтобы запустить новую рабочую область. Как только вы будете готовы отправить свои первые изменения в код, 
Gitpod поможет вам разветвить этот проект, чтобы вы владели им.

### Существующий проект

Чтобы начать работу с Python на Gitpod, добавьте [`.gitpod.yml`](./.gitpod.yml) 
, который содержит конфигурацию для улучшения работы разработчика на Gitpod. 
Чтобы узнать больше, пожалуйста, смотрите 
[Getting Started](https://www.gitpod.io/docs/getting-started) документация.

```shell
python -m pip freeze > requirements.in
pip-compile
rm requirements.in
python -m pip install --upgrade pip requests httpx bs4 
python -m pip install --upgrade 'requests[socks]'
python -m pip install --upgrade 'httpx[socks]'
```