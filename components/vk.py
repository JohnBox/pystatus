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
        Base.__init__(self, cfg['color'])
        try:
            try:
                if VK.skip:
                    VK.skip -= 1
                else:
                    raise Exception
                count = VK.count
                urgent = VK.urgent
            except:
                messages = API(cfg).messages.getDialogs(unread=False)
                count = int(messages['count'])
                urgent = False
                if any(map(lambda i: str(i['message']['user_id']) == cfg['importantid'], messages['items'])):
                    urgent = True
                VK.skip = cfg['refresh']
                VK.count = count
                VK.urgent = urgent
            self.urgent = urgent
            self.full_text = '+{0:d}'.format(count) if count else ''
        except:
            self.full_text = ''

