/*drop table room;
drop table attribute;
drop table resLife;
drop table student;
drop table preferences;
*/
create table room (
       room_code varchar(5) primary key,
       available boolean
);

create table attribute (
       att_id varchar(5) primary key,
       att_label varchar(50),
       necessary boolean
);

create table student (
       username varchar(15) primary key,
       pw varchar(50),
       nm varchar(50),
       yr char(4),
       lottery_num int,
       room_code varchar(5),
       foreign key (room_code) references room(room_code)
);

create table preferences (
username varchar(15),
att_id varchar(5),
primary key (username, att_id),
foreign key (username) references student(username),
foreign key (att_id) references attribute(att_id)
);

create table resLife (
       username varchar(15) primary key,
       pw varchar(50),
       nm varchar(50)
);
/*
insert into resLife (username, pw, nm) values
       ('hpotter', 'h3dw1g', 'Harry Potter'),
       ('hgranger', 'Cr00ksh@nk$', 'Hermione Granger'),
       ('rweasley', 'sc@bb3r%', 'Ron Weasley');


insert into room (room_code, available) values
       ('SHA419', false),
       ('MUN420', true);


insert into attribute(att_id, att_label, necessary) values
       (1,'single', false),
       (2,'nut free', true),
       (3,'carpet', true);


insert into student(username,pw,nm,yr,lottery_num, room_code) values
       ('jyoung4','ch33zit','Jackie Young','018',123,'SHA419'),
       ('dtosca','w00h00','Diana Tosca','2018',321,'BAT409');


insert into preferences (username, att_id) values
       ('jyoung4', 1),
       ('jyoung4', 3),
       ('jyoung4', 5);
*/