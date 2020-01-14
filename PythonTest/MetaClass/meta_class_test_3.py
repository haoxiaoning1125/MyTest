# coding=utf-8
# metaclass 和 ORM


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found mapping: {} ==> {}'.format(k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 表名和类名一致
        attrs['__mappings__'] = mappings  # 保证属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Model object has no attribute {}'.format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields, params, args = [], [], []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = "insert into {} ({}) values ({})".format(
            self.__table__, ','.join(fields), ','.join(params)
        )
        print 'SQL: {}'.format(sql)
        print 'ARGS: {}'.format(str(args))


class User(Model):
    id = IntegerField('id')
    username = StringField('username')
    password = StringField('password')


if __name__ == '__main__':
    user = User(id=1001, username='hao', password='1997')
    user.save()
