class LogRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'logmanager':
            return 'logmanager'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'logmanager':
            return 'logmanager'
        return None

    def allow_syncdb(self, db, model):
        if db == 'logmanager':
            return model._meta.app_label == 'logmanager'
        elif model._meta.app_label == 'logmanager':
            return False
        return None
