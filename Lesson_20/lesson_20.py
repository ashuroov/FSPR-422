'''
git config --global user.name "name in github"
git config --global user.email "real email"

System:
git config --system
Use: git config --global
Project: git config


git config --list: выводит все настройки конфигурации
git config user.name: чтобы вывести определенную конфигурацию
git config --global core.editor - to set editor to open

git init - создание локального пустого репозитория с .git файлом
git status
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ashuroov/FSPR-422.git


Урок 20
fix: Adds lesson_20.py and materials.md
bug:
upd:
del:
'''

"""
Цикл работы с гит:

git status - чтобы узнавать нынешний статус проекта

git add .
git commit -m "message"
git push

git add название_файла
git commit
git push

git remote add origin ссылка_на_репозиторий 
git push --set-upstream origin main
"""

a = 1
b = 2
s = a + b
print(s)