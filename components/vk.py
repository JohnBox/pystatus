from .base import Base
import vk


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class API(metaclass=Singleton):
    def __init__(self, cfg):
            session = vk.AuthSession(app_id=cfg['appid'], user_login=cfg['login'],
                                     user_password=cfg['passwd'], scope=cfg['permission'])
            self.api = vk.API(session, v=cfg['apiv'])

    def __getattr__(self, name):
        return getattr(self.api, name)


class VK(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.count = None
        self.refresh()

    def refresh(self):
        try:
            messages = API(self.cfg).messages.getDialogs(unread=False)
            self.count = int(messages['count'])
            self.urgent = False
            if any(map(lambda i: str(i['message']['user_id']) == self.cfg['importantid'], messages['items'])):
                self.urgent = True

            if self.count:
                self.visible = True
                self.full_text = '+{0:d}'.format(self.count)
            else:
                self.visible = False
        except Exception as e:
            print(e)
            self.full_text = ''


