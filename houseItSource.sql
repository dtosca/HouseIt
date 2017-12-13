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
       hardwood boolean,
       pets_ok boolean,
       acc boolean,
       available boolean,
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
       hardwood boolean,
       pets_ok boolean,
       acc boolean,
       room_code varchar(6),
       foreign key (room_code) references room(room_code)
);

create table admin (
       username varchar(15) primary key,
       nm varchar(50)
);

insert into admin (username, nm) values
       ('hpotter', 'Harry Potter'),
       ('hgranger', 'Hermione Granger'),
       ('rweasley', 'Ron Weasley');

insert into room (room_code, dorm, room_type, hardwood, pets_ok, acc, available,username) values
  ('BAT409','Bates','single',true,true,true,true,NULL),
  ('SHA419','Shafer','single',true,true,true,true,NULL),
  ('FRE108','Freeman','double',false,false,true,true,NULL);

-- insert into student(username, nm, yr, lottery_num, dorm, type, hardwood, pets_ok, accessible, room_code) values
