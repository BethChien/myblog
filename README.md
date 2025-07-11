# myblog

## 安裝 django
```
python3 -m venv myenv
source myenv/bin/activate

pip install django
django-admin --version
```
## 創建新方案
```
cd myblogbeth
django-admin startproject mysite
```

## Starting development server at http://127.0.0.1:8000/
`python manage.py runserver`

## 更新資料庫，根據 manage.py 寫的 model，產生遷移檔 （migration file）
`python manage.py makemigrations`

## 執行 migration file 將遷移檔的變化真正執行到資料庫
`python manage.py migrate`

## 使用最高權限帳號 admin 到後台去看資料庫的狀態
`python manage.py createsuperuser`

## 前往後台 
http://127.0.0.1:8000/admin

## app - django 所有的應用都是以 app 為單位
```
python manage.py startapp <app name>
python mange.py startapp polls
```

# Setting 
- settings 
  * install_apps django 默認預先安裝六個 app
  創建的 app 需要加進入這個設定檔
  * allow_hosts 白名單設定
  * middleware 引入其他 django 套件需要做設定的地方
  * templates 模板設定的位置，已經有預設的模板供你修改
  * time_zone, static_url 時區及靜態檔案（html, css, image...）的設定

- urls
  使用者透過我們預先設定的 urls 進行訪問

- wsgi 同步程式碼設定
- asgi 異步程式碼設定

# 為什麼 Template 需要創建兩層？  
./myblog/mysite/app/templates/app/index.html
為什麼要在創建一個app目錄呢？
因為在 django 裡面會以 app 為單位區分每個功能，例如：首頁，購物車，如果每個 app 下都有 index.html 會無法區分，所以需要在 Templates 目錄下載創建一個與 app 相同的名稱．

# Template 嵌入式語法變數{{}}，語法{%%}
## 變數
  普通變數 {{ var1 }}
  字典變數 {{ dict.var1 }}
## 設定用語法
  {% load static %} 引入靜態文件到該頁面
  {% static 'css/navbar.css' %} 先使用{% load static %}即可引入
  {% static 'js/jquery.js' %}

  需要到 setting.py 貼上以下這段做設定，記得 import os
  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
  ]