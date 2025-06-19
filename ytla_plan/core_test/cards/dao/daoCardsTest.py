import unittest
from core.cards.dao import daoCards
from core.cards.dao.daoCards import Instance, add_card, update_card_detail, soft_delete_card


class TestDaoCards(unittest.TestCase):
    def setUp(self):
        """Initialize test environment"""
        self.test_card = {
            'name': 'Test Card',
            'tags': '',
            'description': '',
            'icon_path': '',
            'background_path': ''
        }
        add_card('test_type', '', self.test_card)
        self.card_id = self._get_last_new_card_id(self.test_card['name'])

    def tearDown(self):
        """Clean up test data"""
        soft_delete_card(self.card_id)

    def _get_last_new_card_id(self, name: str) -> int:
        """Helper method to get the ID of the most recently added test card"""
        sql = "SELECT CARD_ID FROM CARDS WHERE NAME = ? ORDER BY CARD_ID DESC LIMIT 1"
        res = daoCards.execute_cursor(sql, (name,))
        return res[0]['CARD_ID']

    def test_1_add_card(self):
        """Test adding a new card"""
        new_card = {
            'name': 'New Test Card',
            'tags': '',
            'description': '',
            'icon_path': '',
            'background_path': ''
        }
        add_card('test_type', '', new_card)
        new_id = self._get_last_new_card_id(new_card['name'])
        self.assertGreater(new_id, self.card_id)

    def test_2_update_card_detail(self):
        """Test updating card details"""
        updated_card = Instance('Updated Card', 'test_type')
        updated_card.card_id = self.card_id
        updated_card.description = "Updated description"
        update_card_detail(updated_card)

        # Verify the updated data
        check_sql = "SELECT DESCRIPTION FROM CARDS WHERE CARD_ID = ?"
        result = daoCards.execute_cursor(check_sql, (self.card_id,))
        self.assertEqual(result[0]['DESCRIPTION'], "Updated description")

    def test_3_activate_deactivate(self):
        """Test card activation/deactivation workflow"""
        from core.cards.dao.daoCards import deactivate_card, check_card_active_status

        deactivate_card(self.card_id)
        self.assertEqual(check_card_active_status(self.card_id), '0')

        # Note: Unlike plans, cards don't have an activate_card function in the original
        # If you need activation functionality, you should add it to daoCards.py first

    def test_4_soft_delete(self):
        """Test soft deletion of card"""
        soft_delete_card(self.card_id)
        check_sql = "SELECT DELETE_FLAG FROM CARDS WHERE CARD_ID = ?"
        result = daoCards.execute_cursor(check_sql, (self.card_id,))
        self.assertEqual(result[0]['DELETE_FLAG'], '1')


if __name__ == '__main__':
    unittest.main()
