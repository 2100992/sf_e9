from app import app, db

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app.models import Forecast, User


migrate = Migrate(app, db)

# Инициализируем менеджер
manager = Manager(app)

# Регистрируем команду, реализованную в виде потока
# класса COmmand
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell)


if __name__ == "__main__":
    manager.run()
