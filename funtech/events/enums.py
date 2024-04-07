from enum import Enum


class EventTypeEnum(Enum):
    OFFLINE = 'Оффлайн'
    ONLINE = 'Онлайн'


class EventFormatEnum(Enum):
    CONFERENCE = 'Конференция'
    MEETUP = 'Митап'
    NETWORKING = 'Нетворкинг'
    EXCURSION = 'Экскурсия'


class EventStatusEnum(Enum):
    REGISTRATION_OPEN = 'Регистрация открыта'
    REGISTRATION_CLOSE = 'Регистрация закрыта'
    FINISHED = 'Завершено'


class EventActivityStatusEnum(Enum):
    DRAFT = 'Черновик'
    ACTIVE_EVENT = 'Активное мероприятие'


class EventThemeEnum(Enum):
    PROGRAMMING = 'Разработка'
    DESIGN = 'Дизайн '
    MANAGEMENT = 'Менеджмент'
    MARKETING = 'Маркетинг'
    ANALYTICS = 'Аналитика'
    BUSINESS = 'Бизнес'
    OTHER = 'Другое'
