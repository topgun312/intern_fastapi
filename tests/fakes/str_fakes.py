import datetime

from src.schemas.str_schema import SpimexTradingResultsSchema

FAKE_RESULTS: list[SpimexTradingResultsSchema] = [
    SpimexTradingResultsSchema(
        id=1,
        exchange_product_id="A100NVY060F",
        exchange_product_name="Бензин (АИ-100-К5), ст. Новоярославская (ст. отправления)",
        oil_id="A100",
        delivery_basis_id="NVY",
        delivery_basis_name="ст. Новоярославская",
        delivery_type_id="F",
        volume="60",
        total="5646120",
        count="1",
        date=datetime.date(2024, 7, 23),
    ),
    SpimexTradingResultsSchema(
        id=2,
        exchange_product_id="A100NVQ960F",
        exchange_product_name="Бензин (АИ-100-К5), ст. Новоярославская (ст. отправления)",
        oil_id="A100",
        delivery_basis_id="NVQ",
        delivery_basis_name="ст. Новоярославская",
        delivery_type_id="F",
        volume="60",
        total="5646120",
        count="1",
        date=datetime.date(2024, 7, 24),
    ),
    SpimexTradingResultsSchema(
        id=3,
        exchange_product_id="A592ACH005A",
        exchange_product_name="Бензин (АИ-92-К5) по ГОСТ, Ачинский НПЗ (самовывоз автотранспортом)",
        oil_id="A592",
        delivery_basis_id="ACH",
        delivery_basis_name="Ачинский НПЗ",
        delivery_type_id="A",
        volume="75",
        total="4757625",
        count="3",
        date=datetime.date(2024, 7, 25),
    ),
    SpimexTradingResultsSchema(
        id=4,
        exchange_product_id="DSC5LUL065E",
        exchange_product_name="ДТ ЕВРО сорт C (ДТ-Л-К5) минус 5, Волгоград-группа станций (ст. отправления)",
        oil_id="DSC5",
        delivery_basis_id="LUL",
        delivery_basis_name="Волгоград-группа станций",
        delivery_type_id="E",
        volume="4485",
        total="280612995",
        count="19",
        date=datetime.date(2024, 7, 26),
    ),
]
