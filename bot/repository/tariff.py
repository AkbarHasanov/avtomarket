from bot.database.session import db
from bot.models.tariff import Translation, Tariff


def get_tariffs():
    return db.query(Tariff).all()


def get_translation(tariff_id, language) -> Translation:
    return db.query(Translation).filter_by(tariff_id=tariff_id, language=language).first()


def init_tariffs():
    db.add_all([
        Tariff(
            amount=49000,
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
