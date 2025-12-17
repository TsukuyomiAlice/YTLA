# encode = utf-8

from core.domain.area.users.dao import daoUser
from core.domain.area.plans.dao import daoPlans
from core.domain.area.modules.dao import daoModules
from core.domain.area.frame.dao import daoGlobalPersistence
from core.domain.area.cards.dao import daoCards


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
