# encode = utf-8

from core.classic.users.dao import daoUser
from core.classic.plans.dao import daoPlans
from core.classic.modules.dao import daoModules
from core.classic.frame.dao import daoGlobalPersistence
from core.classic.cards.dao import daoCards


def clean_initiate():
    daoCards.drop_table()
    daoCards.create_table()
    daoPlans.drop_table()
    daoPlans.create_table()
    daoModules.drop_table()
    daoModules.create_table()
    daoGlobalPersistence.drop_table()
    daoGlobalPersistence.create_table()
    daoUser.drop_table()
    daoUser.create_table()


def initiate():
    daoCards.create_table()
    daoPlans.create_table()
    daoModules.create_table()
    daoGlobalPersistence.create_table()
    daoUser.create_table()


if __name__ == '__main__':
    initiate()
