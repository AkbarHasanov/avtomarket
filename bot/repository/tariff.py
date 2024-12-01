from bot.database.session import get_db
from bot.models.tariff import Translation, Tariff
from const import *


def get_tariffs():
    db = next(get_db())
    return db.query(Tariff).all()


def get_translation(tariff_id, language) -> Translation:
    get_db()
    return db.query(Translation).filter_by(tariff_id=tariff_id, language=language).first()


def get_by_callback_data(callback_data):
    get_db()
    return db.query(Tariff).filter_by(callback_data=callback_data).first()

def init_tariffs():
    get_db()
    db.add_all([
        Tariff(
            amount=49000,
            callback_data=CALLBACK_DATA_ECONOMIC,
            translations=[
                Translation(
                    name='Эконом',
                    title='Эконом',
                    description='Эконом',
                    language='RU',
                    label='Эконом',
                ),
                Translation(
                    name='Iqtisodiyot',
                    title='Iqtisodiyot',
                    description='Iqtisodiyot',
                    language='UZ',
                    label='Iqtisodiyot',
                ),
            ],
        ),
        Tariff(
            amount=59000,
            callback_data=CALLBACK_DATA_STANDARD,
            translations=[
                Translation(
                    name='Стандарт',
                    title='Стандарт',
                    description='Стандарт',
                    language='RU',
                    label='Стандарт',
                ),
                Translation(
                    name='Standart',
                    title='Standart',
                    description='Standart',
                    language='UZ',
                    label='Standart',
                ),
            ],
        ),
        Tariff(
            amount=69000,
            callback_data=CALLBACK_DATA_PREMIUM,
            translations=[
                Translation(
                    name='Премиум',
                    title='Премиум',
                    description='Премиум',
                    language='RU',
                    label='Премиум',
                ),
                Translation(
                    name='Premium',
                    title='Premium',
                    description='Premium',
                    language='UZ',
                    label='Premium',
                ),
            ],
        ),
        Tariff(
            amount=89000,
            callback_data=CALLBACK_DATA_ELITE,
            translations=[
                Translation(
                    name='Элитный',
                    title='Элитный',
                    description='Элитный',
                    language='RU',
                    label='Элитный',
                ),
                Translation(
                    name='Elite',
                    title='Elite',
                    description='Elite',
                    language='UZ',
                    label='Elite',
                ),
            ],
        ),
        Tariff(
            amount=129000,
            callback_data=CALLBACK_DATA_EXCLUSIVE,
            translations=[
                Translation(
                    name='Эксклюзив',
                    title='Эксклюзив',
                    description='Эксклюзив',
                    language='RU',
                    label='Эксклюзив',
                ),
                Translation(
                    name='Eksklyuziv',
                    title='Eksklyuziv',
                    description='Eksklyuziv',
                    language='UZ',
                    label='Eksklyuziv',
                ),
            ],
        ),
        Tariff(
            amount=189000,
            callback_data=CALLBACK_DATA_EXTREME,
            translations=[
                Translation(
                    name='Экстрим',
                    title='Экстрим',
                    description='Экстрим',
                    language='RU',
                    label='Экстрим',
                ),
                Translation(
                    name='Ekstremal',
                    title='Ekstremal',
                    description='Ekstremal',
                    language='UZ',
                    label='Ekstremal',
                ),
            ],
        ),
    ])
    db.commit()
