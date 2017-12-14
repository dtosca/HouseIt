drop table student;
drop table room;
drop table admin;

create table room (
       room_code varchar(6) primary key,
       dorm enum('Beebe', 'Cazenove', 'Munger', 'Pomeroy', 'Shafer', 
              'Claflin', 'Lake House', 'Severance', 'Tower Court', 
             'Bates', 'Freeman','McAfee','Casa Cervantes','Dower',
              'French House','Stone-Davis', 'Simpson West', 'Hemlock'),
       room_type enum('single', 'double', 'triple', 'quad', 'suite'),
       nuts boolean,
       hardwood boolean,
       pets boolean,
       acc boolean,
       available boolean
);

create table student (
       username varchar(15) primary key,
       nm varchar(50),
       yr char(4),
       lottery_num int,
       dorm enum('Beebe', 'Cazenove', 'Munger', 'Pomeroy', 'Shafer', 
              'Claflin', 'Lake House', 'Severance', 'Tower Court', 
              'Bates', 'Freeman','McAfee','Casa Cervantes','Dower',
              'French House','Stone-Davis', 'Simpson West', 'Hemlock'),
       room_type enum('single', 'double', 'triple', 'quad', 'suite'),
       nuts boolean,
       hardwood boolean,
       pets boolean,
       acc boolean,
       room_code varchar(6),
       foreign key (room_code) references room(room_code)
);

insert into room (room_code, dorm, room_type, nuts, hardwood, pets, acc, available) values
  ('BAT409','Bates','single',true,false,true,false,true),
  ('BAT419','Bates','single',true,false,true,false,true),
  ('BAT429','Bates','single',true,false,true,false,true),
  ('BAT459','Bates','single',true,false,true,false,true),
  ('BAT439','Bates','single',true,false,true,false,true),
  ('BAT449','Bates','single',true,false,true,false,true),
  ('BAT408','Bates','single',false,false,false,false,true),
  ('BAT407','Bates','single',false,false,true,false,true),
  ('BAT406','Bates','single',true,false,false,false,true),
  ('BAT405','Bates','single',false,true,false,true,true),
  ('BAT404','Bates','single',false,false,true,true,true),
  ('BAT403','Bates','single',true,true,false,false,true),
  ('BAT402','Bates','single',true,false,true,false,true),
  ('BAT401','Bates','single',true,false,true,false,true),
  ('BAT309','Bates','double',false,true,false,true,true),
  ('BAT209','Bates','single',true,false,false,true,true),
  ('BAT109','Bates','double',false,false,true,true,true),
  ('BAT009','Bates','single',true,true,false,false,true),
  ('SHA419','Shafer','single',false,false,true,true,true),
  ('SHA319','Shafer','single',true,false,false,true,true),
  ('SHA219','Shafer','single',false,true,true,true,true),
  ('SHA119','Shafer','single',true,false,true,true,true),
  ('SHA019','Shafer','single',true,true,false,true,true),
  ('FRE408','Freeman','double',false,false,false,true,true),
  ('FRE308','Freeman','single',false,true,false,true,true),
  ('FRE208','Freeman','double',true,true,false,true,true),
  ('FRE108','Freeman','single',true,true,false,true,true),
  ('FRE008','Freeman','double',false,true,true,true,true),
  ('TOW423','Tower Court','double',false,true,true,false,true),
  ('TOW323','Tower Court','double',false,true,false,true,true),
  ('TOW223','Tower Court','double',false,false,true,true,true),
  ('TOW123','Tower Court','double',false,false,false,true,true),
  ('TOW023','Tower Court','double',false,true,false,true,true);