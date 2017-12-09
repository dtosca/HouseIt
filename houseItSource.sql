drop table preferences;
drop table student;
drop table room;
drop table attribute;
drop table resLife;

create table room (
       room_code varchar(6) primary key,
       available boolean
);

create table attribute (
       att_id int not null primary key auto_increment,
       att_label varchar(50),
       necessary boolean
);

create table student (
       username varchar(15) primary key,
       pw varchar(50),
       nm varchar(50),
       yr char(4),
       lottery_num int,
       room_code varchar(6),
       foreign key (room_code) references room(room_code)
);

create table preferences (
       username varchar(15),
       att_id int,
       primary key (username, att_id),
       foreign key (username) references student(username),
       foreign key (att_id) references attribute(att_id)
);

create table resLife (
       username varchar(15) primary key,
       pw varchar(50),
       nm varchar(50)
);

insert into resLife (username, pw, nm) values
       ('hpotter', 'h3dw1g', 'Harry Potter'),
       ('hgranger', 'Cr00ksh@nk$', 'Hermione Granger'),
       ('rweasley', 'sc@bb3r%', 'Ron Weasley');


insert into room (room_code, available) values
       ('SHA419', false),
       ('BAT409', true);


insert into attribute(att_label, necessary) values
       ('single', false),
       ('double',false),
       ('triple',false),
       ('quad',false),
       ('nut free', true),
       ('non carpet', true),
       ('pet free',true);


insert into student(username,pw,nm,yr,lottery_num, room_code) values
       ('jyoung4','ch33zit','Jackie Young','018',123,'SHA419'),
       ('dtosca','w00h00','Diana Tosca','2018',321,'BAT409');