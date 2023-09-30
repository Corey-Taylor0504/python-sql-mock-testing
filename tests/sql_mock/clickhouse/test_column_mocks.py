from sql_mock.clickhouse.column_mocks import ClickhouseColumnMock, Decimal

def test_init_not_nullable():
    """
    ...then nullable should be False and dtype be the same as passed.
    """

    class ColMock(ClickhouseColumnMock):
        dtype = "Integer"

    column = ColMock(default=42)

    assert column.default == 42
    assert column.dtype == "Integer"
    assert not column.nullable

def test_init_nullable():
    """
    ...then nullable should be True and dtype should be wrapped with "Nullable()"
    """

    class ColMock(ClickhouseColumnMock):
        dtype = "Integer"

    column = ColMock(default=42, nullable=True)

    assert column.default == 42
    assert column.dtype == "Nullable(Integer)"
    assert column.nullable

def test_decimal_initialization_not_nullable():
    """Ensure that the Decimal object is initialized correctly."""
    decimal_col = Decimal(default=0.0, precision=10, scale=2, nullable=False)
    assert decimal_col.dtype == "Decimal(10, 2)"
    assert decimal_col.default == 0.0
    assert not decimal_col.nullable

def test_decimal_initialization_nullable():
    """Ensure that the Decimal object is initialized correctly."""
    decimal_col = Decimal(default=0.0, precision=10, scale=2, nullable=True)
    assert decimal_col.dtype == "Nullable(Decimal(10, 2))"
    assert decimal_col.default == 0.0
    assert decimal_col.nullable
