from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class UserModel(db.Model, UserMixin):
    __tablename__ = 'cp_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), comment='用户名')
    realname = db.Column(db.String(20), comment='真实名字')
    mobile = db.Column(db.String(11), comment='电话号码')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    comment = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    dept_id = db.Column(db.Integer, comment='部门id')

    role = db.relationship('RoleModel', secondary="rt_user_role", backref=db.backref('user'), lazy='dynamic')

    def set_password(self, password):
        """设置密码，对密码进行加密存储"""
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        """校验密码方法"""
        return check_password_hash(self.password_hash, password)

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class DepartmentModel(db.Model):
    __tablename__ = 'cp_dept'
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    parent_id = db.Column(db.Integer, comment="父级编号")
    dept_name = db.Column(db.String(50), comment="部门名称")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    status = db.Column(db.Boolean, comment='状态(1开启,0关闭)')
    comment = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
    sort = db.Column(db.Integer, comment="排序")

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

class FsModels(db.Model):
    __tablename__ = 'cp_fs'
    id = db.Column(db.Integer, primary_key=True, comment="报表ID")
    name = db.Column(db.String(50), comment="报表名称")
    all_num = db.Column(db.Integer, default=0, comment="样本总数")
    fraud_num = db.Column(db.Integer, default=0, comment="欺诈样本")
    nonfraud_num = db.Column(db.Integer, default=0, comment="非欺诈样本")

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

class FdModels(db.Model):
    __tablename__ = 'cp_fd'
    id = db.Column(db.Integer, primary_key=True, comment="文件ID")
    name = db.Column(db.String(50), comment="文件名称")
    # mime = db.Column(db.CHAR(50), nullable=False, comment="文件类型")
    size = db.Column(db.CHAR(30), nullable=False, comment="文件大小")
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

class PtModels(db.Model):
    __tablename__ = 'cp_pt'
    id = db.Column(db.String(30), primary_key=True, comment="资产编码")
    name = db.Column(db.String(50), comment="设备名称")
    total = db.Column(db.Integer, comment="总数")
    other = db.Column(db.DateTime, default=datetime.now, comment='其他描述')

class MatchModels(db.Model):
    __tablename__ = 'cp_match'
    id = db.Column(db.String(30), primary_key=True, comment="资产编码")
    name = db.Column(db.String(50), comment="设备名称")
    num = db.Column(db.Integer, comment="同类型总数量")
    place = db.Column(db.String(50), comment="存放安装地点")
    first = db.Column(db.String(50), comment="一级")
    second = db.Column(db.String(50), comment="二级")
    rangee = db.Column(db.String(50), comment="其他描述/取值范围")
    unit = db.Column(db.String(50), comment="单位")
    original = db.Column(db.String(50), comment="原值")