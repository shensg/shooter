## Shooter
* 这是一个开源的简洁的运维平台，笔者是个非常懒惰的人
* 此项目采用了前后端分离，支持二次开发
* 有新的需求可以在issue留下你的问题或者笔者遗漏了实用的功能，笔者会仔细阅读。至于会不会解决得看笔者的心情了
* 笔者的开发能力有限，代码有点地方写的不太优雅。同时也有能力的小伙伴积极加入这个开源项目
* 开源不易，希望大家给个star支持下笔者持续维护

### 这是一个运维平台
1. 已经简单的运维平台，集成云原生
2. 使用非常简单，小白轻松上手

### 部署要求
服务器要求：2C4G, Python版本：3.12+

### 部署项目
默认账号密码
username: admin
password: shooter123

#### docker部署
```shell
# change director, clone git repo
cd /opt
git checkout master
docker-compose pull -f docker-compose.yml
docker-compose up -f docker-compose.yml -d
docker exec -i shooter-shooter-1 python create_table.py
docker exec -i shooter-shooter-1 python sql.py
```

#### 服务器部署
```shell
# change director, clone git repo
cd /opt
git checkout master
```
