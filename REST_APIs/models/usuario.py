from sql_alchemy import banco

class UsuarioModel(banco.Model):
    __tablename__ = 'usuarios'

    usuario_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(50))
    senha = banco.Column(banco.String(50))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def json(self):
        return{
            'usuario_id': self.usuario_id,
            'login': self.login
        }
    
    @classmethod
    def buscar_usuario(cls, usuario_id):
        usuario = cls.query.filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None
    
    def save_usuario(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_usuario(self):
        banco.session.delete(self)
        banco.session.commit()