import pytest
from DSL.util.logger import get_core_logger
from DSL.API.database import userDatabase

@pytest.mark.database
class TestDatabase:
    logger = get_core_logger("database_test")
    values = [
        ['0', '郑金亮', '19', '0', '10086', ],
        ['1', '郑金亮二号', '20', '1000', '10001'],
        ['2', '郑金亮三号', '21', '100000', '10000']
    ]
    def test_init(self):
        self.database = userDatabase()

    @pytest.mark.insertdata
    def test_add_value(self):
        for value in self.values:
            self.database.insert_value(value)
    
    def test_select(self):
        for i in range(2):
            result = self.database.select_with_id(str(i))
            self.logger.info(result)

if __name__ == '__main__':
    test = TestDatabase()
    test.test_init()
    test.test_add_value()
    test.test_select()
