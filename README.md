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

```
    # print(soup.prettify())
    # print(soup.find_all('a'))

    # limits = httpx.Limits(max_keepalive_connections=30, max_connections=10)
```
```
# with requests.Session(proxies="http://localhost:9050") as s:
#     r = s.get(url, headers=headers, params=querystring)
#     print(r)

# proxies = {"all": "socks5://127.0.0.1:9050"}
```

```html
<div class="pag_navigation">
        <div class="wrp">
         <ul class="pagination">
          <li>
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=1">
            1
           </a>
          </li>
          <li class="active">
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=2">
            2
           </a>
          </li>
          <li>
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=3">
            3
           </a>
          </li>
          <li>
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=4">
            4
           </a>
          </li>
          <li>
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=5">
            5
           </a>
          </li>
          <li>
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=6">
            6
           </a>
          </li>
          <li class="pag_left">
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=1">
            <i class="i_left">
            </i>
           </a>
          </li>
          <li class="pag_right">
           <a href="http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/catalog/2?query=&amp;sort_direction=desc&amp;sort=rate&amp;page=3">
            <i class="i_right">
            </i>
           </a>
          </li>
         </ul>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
```