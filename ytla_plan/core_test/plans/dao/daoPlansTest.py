import unittest
from core.domain.area.plans.dao import daoPlans
from core.domain.area.plans.dao.daoPlans import Instance, add_plan, update_plan_detail, soft_delete_plan, get_last_new_plan_id


class TestDaoPlans(unittest.TestCase):
    def setUp(self):
        """Initialize test environment"""
        self.test_plan = Instance("测试计划")
        self.test_plan.detail_params = '{}'
        add_plan(self.test_plan)
        self.plan_id = get_last_new_plan_id()

    def tearDown(self):
        """Clean up test data"""
        soft_delete_plan(self.plan_id)

    def test_1_add_plan(self):
        """Test adding a new plan"""
        new_plan = Instance("a new plan")
        add_plan(new_plan)
        new_id = get_last_new_plan_id()
        self.assertGreater(new_id, self.plan_id)

    def test_2_update_plan_detail(self):
        """Test updating plan details"""
        updated_plan = Instance("updated plan")
        updated_plan.plan_id = self.plan_id
        updated_plan.description = "updated description"
        update_plan_detail(updated_plan)

        # 验证更新后的数据
        check_sql = "SELECT DESCRIPTION FROM PLANS WHERE plan_id = ?"
        result = daoPlans.execute_cursor(check_sql, (self.plan_id,))
        self.assertEqual(result[0]['DESCRIPTION'], "updated description")

    def test_3_activate_deactivate(self):
        """Test plan activation/deactivation workflow"""
        from core.domain.area.plans.dao.daoPlans import deactivate_plan, activate_plan, check_plan_active_status

        deactivate_plan(self.plan_id)
        self.assertEqual(check_plan_active_status(self.plan_id), '0')

        activate_plan(self.plan_id)
        self.assertEqual(check_plan_active_status(self.plan_id), '1')

    def test_4_soft_delete(self):
        """Test soft deletion of plan"""
        soft_delete_plan(self.plan_id)
        check_sql = "SELECT DELETE_FLAG FROM PLANS WHERE plan_id = ?"
        result = daoPlans.execute_cursor(check_sql, (self.plan_id,))
        self.assertEqual(result[0]['DELETE_FLAG'], '1')


if __name__ == '__main__':
    unittest.main()