#!/usr/bin/env python2.7
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base

#sys.path.append('/home/eshufan/project/drcontroller/drcontroller/db')

Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)
'''
Models for DRGlance, DRNeutron, DRNova
'''
class DRGlance(Base):
    '''
    Model class DRGlance
    '''
    __tablename__ = "dr_glance"

    id = Column(Integer, Sequence('dr_glance_id_seq'), primary_key = True)
    primary_uuid = Column(String(50))
    secondary_uuid = Column(String(50))
    status = Column(String(20))
    other = Column(String(50))

    def __repr__(self):
        return "<DRGlance(primary_uuid = '%s', secondary_uuid = '%s', status = '%s', other = '%s')>" % (self.primary_uuid, self.secondary_uuid, self.status, self.other)


class DRNeutron(Base):
    '''
    Model class DRNeutron
    '''
    __tablename__ = "dr_neutron"

    id = Column(Integer, Sequence('dr_neutron_id_seq'), primary_key = True)
    primary_uuid = Column(String(50))
    secondary_uuid = Column(String(50))
    status = Column(String(20))
    deleted_flag = Column(String(2))
    other =  Column(String(50))

    def __repr__(self):
        return "<DRNeutron(primary_uuid = '%s', secondary_uuid = '%s', status = '%s', deleted_flag = '%s', other = '%s')>" %\
                (self.primary_uuid, self.secondary_uuid, self.status, self.deleted_flag, self.other)

class DRNeutronSubnet(Base):
    '''
    Model class DRNeutronSubnet.
    '''
    __tablename__ = "dr_neutron_subnet"

    id = Column(Integer, Sequence('dr_neutron_id_seq'), primary_key = True)
    primary_uuid = Column(String(50))
    secondary_uuid = Column(String(50))
    status = Column(String(20))
    deleted_flag = Column(String(2))
    # network_id  relate to DRNeutron.secondary_uuid
    network_id = Column(String(50))
    other =  Column(String(50))

    def __repr__(self):
        return "<DRNeutronSubnet(network_id = %s, primary_uuid = '%s', secondary_uuid = '%s', status = '%s',deleted_flag = '%s', other = '%s')>" %\
                (self.network_id, self.primary_uuid, self.secondary_uuid, self.status, self.deleted_flag, self.other)

class DRNeutronPort(Base):
    '''
    Model Class DRNeutronPort.
    '''
    __tablename__ = "dr_neutron_port"
    id = Column(Integer, Sequence('dr_neutron_id_seq'), primary_key = True)
    primary_uuid = Column(String(50))
    secondary_uuid = Column(String(50))
    primary_floatingip_uuid = Column(String(50))
    secondary_floatingip_uuid = Column(String(50))
    floating_ip_address = Column(String(30))
    deleted_flag = Column(String(2))
    other =  Column(String(50))

    def __repr__(self):
        return "<DRNeutronPort(primary_uuid = '%s', secondary_uuid = '%s', primary_floatingip_uuid = '%s', secondary_floatingip_uuid ='%s',floating_ip_address ='%s', deleted_flag = '%s', other = '%s')>" %\
                 (self.primary_uuid, self.secondary_uuid,self.primary_floatingip_uuid,self.secondary_floatingip_uuid,self.floating_ip_address, self.deleted_flag, self.other)

class DRNova(Base):
    '''
    Model Class DRNova
    '''
    __tablename__ = "dr_nova"

    id = Column(Integer, Sequence('dr_nova_id_seq'), primary_key = True)
    primary_instance_uuid = Column(String(50))
    secondary_instance_uuid = Column(String(50))
    primary_image_uuid = Column(String(50))
    secondary_image_uuid = Column(String(50))
    primary_node_name = Column(String(50))
    secondary_node_name = Column(String(50))
    status = Column(String(20))
    other = Column(String(50))

    def __repr__(self):
        return "<DRNova(primary_instance_uuid = '%s', secondary_instance_uuid = '%s',primary_image_uuid = '%s', secondary_image_uuid = '%s,\
            primary_node_name = '%s',secondary_node_name ='%s', status = '%s', other = '%s')>" % \
            (self.primary_instance_uuid, self.secondary_instance_uuid, self.primary_image_uuid, self.secondary_image_uuid, self.primary_node_name,\
             self.secondary_node_name, self.status, self.other)


