# 実行方法
```sh
# postgresqlのユーザー、パスワードを指定
export DB_USER=XXXX
export DB_PASSWORD=XXXX
# 開発環境用の設定ファイルを指定
export DJANGO_SETTINGS_MODULE=private_diary.settings_dev

# 初回起動前にmigrationは実施
python manage.py makemigrations
python manage.py migrate

#　サーバの起動
python manage.py runserver
```